import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChamadosDetalhe } from './chamados-detalhe';

describe('ChamadosDetalhe', () => {
  let component: ChamadosDetalhe;
  let fixture: ComponentFixture<ChamadosDetalhe>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ChamadosDetalhe],
    }).compileComponents();

    fixture = TestBed.createComponent(ChamadosDetalhe);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
