// Enhanced frontend JavaScript for sardonic caveman integration
class SardonicCavemanApp {
    constructor() {
        this.lastShownFacts = [];
        this.isLoading = false;
        this.init();
    }

    init() {
        // Auto-load sardonic facts on page load
        setTimeout(() => this.fetchWisdom(), 1500);
        
        // Add keyboard shortcut (Space bar)
        document.addEventListener('keydown', (e) => {
            if (e.code === 'Space' && !this.isLoading) {
                e.preventDefault();
                this.fetchWisdom();
            }
        });
    }

    async fetchWisdom() {
        if (this.isLoading) return;
        
        const factsContainer = document.getElementById('facts');
        const button = document.getElementById('wisdom-btn') || document.querySelector('button');
        
        this.isLoading = true;
        
        // Update UI
        if (button) {
            button.disabled = true;
            button.textContent = 'Unga bunga thinking...';
        }
        if (factsContainer) {
            factsContainer.classList.add('loading');
        }
        
        try {
            // Fetch sardonic caveman facts
            const response = await fetch('/api/facts?count=5');
            if (!response.ok) throw new Error('Cave spirits angry');
            
            const data = await response.json();
            
            // Clear existing facts
            if (factsContainer) {
                factsContainer.innerHTML = '';
                
                // Add new facts with animation
                data.facts.forEach((fact, index) => {
                    setTimeout(() => {
                        this.addFactWithAnimation(factsContainer, fact);
                    }, index * 150);
                });
            }
            
        } catch (error) {
            console.error('❌ Wisdom gathering failed:', error);
            this.showError('Cave spirits too sarcastic today. Try again!');
        } finally {
            // Restore UI
            setTimeout(() => {
                if (button) {
                    button.disabled = false;
                    button.textContent = 'Fetch Wisdom';
                }
                if (factsContainer) {
                    factsContainer.classList.remove('loading');
                }
                this.isLoading = false;
            }, 1000);
        }
    }

    addFactWithAnimation(container, fact) {
        const factElement = document.createElement('p');
        factElement.className = 'fact';
        factElement.textContent = fact.story;
        factElement.style.opacity = '0';
        factElement.style.transform = 'translateY(20px)';
        factElement.style.transition = 'all 0.4s ease';
        
        // Add metadata if available
        if (fact.reliability) {
            factElement.title = `${fact.reliability} | Sources: ${fact.sources}`;
        }
        
        container.appendChild(factElement);
        
        // Trigger animation
        setTimeout(() => {
            factElement.style.opacity = '1';
            factElement.style.transform = 'translateY(0)';
        }, 10);
    }

    showError(message) {
        const factsContainer = document.getElementById('facts');
        if (factsContainer) {
            factsContainer.innerHTML = `
                <p class="fact" style="border-left-color: #d32f2f; background: rgba(211, 47, 47, 0.1);">
                    ${message}
                </p>
            `;
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.sardonicApp = new SardonicCavemanApp();
});

// Global function for backward compatibility
function fetchWisdom() {
    if (window.sardonicApp) {
        window.sardonicApp.fetchWisdom();
    }
}

// Console messages
console.log('🦴 Sardonic Caveman Frontend Ready!');
console.log('💡 Press SPACE to fetch new wisdom');
console.log('😏 Unga bunga ready to be sarcastic about history');
