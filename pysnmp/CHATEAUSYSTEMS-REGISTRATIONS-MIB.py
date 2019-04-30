#
# PySNMP MIB module CHATEAUSYSTEMS-REGISTRATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHATEAUSYSTEMS-REGISTRATIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Unsigned32, IpAddress, MibIdentifier, ObjectIdentity, enterprises, TimeTicks, iso, Bits, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Unsigned32", "IpAddress", "MibIdentifier", "ObjectIdentity", "enterprises", "TimeTicks", "iso", "Bits", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chateausystems = ModuleIdentity((1, 3, 6, 1, 4, 1, 10910))
chateausystems.setRevisions(('2005-11-09 00:00', '2002-02-20 00:00',))
if mibBuilder.loadTexts: chateausystems.setLastUpdated('200511090000Z')
if mibBuilder.loadTexts: chateausystems.setOrganization('Chateau Systems, Inc.')
chateauExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 1))
if mibBuilder.loadTexts: chateauExperimental.setStatus('current')
chateauRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2))
if mibBuilder.loadTexts: chateauRegistrations.setStatus('current')
chateauGlobalRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 1))
if mibBuilder.loadTexts: chateauGlobalRegistrations.setStatus('current')
chateauProductRegs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 1, 1))
if mibBuilder.loadTexts: chateauProductRegs.setStatus('current')
chateauConsumerProductRegs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 1, 1, 3))
if mibBuilder.loadTexts: chateauConsumerProductRegs.setStatus('current')
chateauCDProductReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 1, 1, 3, 1))
if mibBuilder.loadTexts: chateauCDProductReg.setStatus('current')
chateauProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 2))
if mibBuilder.loadTexts: chateauProducts.setStatus('current')
chateauConsumerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 2, 3))
if mibBuilder.loadTexts: chateauConsumerProducts.setStatus('current')
chateauCDProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1))
if mibBuilder.loadTexts: chateauCDProduct.setStatus('current')
class ChateauTrapControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("trapEnable", 1), ("trapDisable", 2))

class ChateauEventSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("major", 4))

mibBuilder.exportSymbols("CHATEAUSYSTEMS-REGISTRATIONS-MIB", ChateauTrapControl=ChateauTrapControl, PYSNMP_MODULE_ID=chateausystems, chateauCDProduct=chateauCDProduct, chateauProducts=chateauProducts, chateauRegistrations=chateauRegistrations, ChateauEventSeverity=ChateauEventSeverity, chateauGlobalRegistrations=chateauGlobalRegistrations, chateausystems=chateausystems, chateauProductRegs=chateauProductRegs, chateauConsumerProducts=chateauConsumerProducts, chateauConsumerProductRegs=chateauConsumerProductRegs, chateauExperimental=chateauExperimental, chateauCDProductReg=chateauCDProductReg)
