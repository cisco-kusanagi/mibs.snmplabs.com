#
# PySNMP MIB module CHATEAUSYSTEMS-REGISTRATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHATEAUSYSTEMS-REGISTRATIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:48:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, MibIdentifier, iso, ModuleIdentity, Unsigned32, Counter32, NotificationType, Gauge32, Bits, ObjectIdentity, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "MibIdentifier", "iso", "ModuleIdentity", "Unsigned32", "Counter32", "NotificationType", "Gauge32", "Bits", "ObjectIdentity", "Integer32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chateausystems = ModuleIdentity((1, 3, 6, 1, 4, 1, 10910))
chateausystems.setRevisions(('2005-11-09 00:00', '2002-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: chateausystems.setRevisionsDescriptions(('Added Consumer CD Product Nodes.', 'First Release.',))
if mibBuilder.loadTexts: chateausystems.setLastUpdated('200511090000Z')
if mibBuilder.loadTexts: chateausystems.setOrganization('Chateau Systems, Inc.')
if mibBuilder.loadTexts: chateausystems.setContactInfo('Larry R. Walsh Chateau Systems, Inc PO Box 898 Stanwood, WA 98292 USA 360 387-2615 larrywalsh@chateausystems.com www.chateausystems.com')
if mibBuilder.loadTexts: chateausystems.setDescription("This MIB defines high level nodes that are used to organize Chateau Systems Registrations and MIBs into ordered groups. This MIB also contains Chateau Systems Enterprise-specific Textual Convention definitions. This MIB is intended to be IMPORT'ed by all other Chateau Systems MIBs. This MIB has been distributed as part of the handout materials from the SNMP Technology Seminar presented by Chateau Systems. Any person or organization making use of this example MIB is responsible for ensuring its complete suitability for their own purposes. This includes the text of the legal disclaimers below, as well as all other aspects. Chateau Systems reserves the right to make changes in specifications and other information contained in this document without prior notice. The reader should contact Chateau Systems to determine whether or not such changes have been made. In no event shall Chateau Systems be liable for any incidental, indirect, special, or consequential damages whatsoever (including but not limited to lost profits) arising out of or related to this document or the information contained in it, even if Chateau Systems has been advised of, known, or should have known, the possibility of such damages. Chateau Systems grants vendors, end-users, and other interested parties a non-exclusive license to use this specification in connection with the management of Chateau Systems products. Copyright November 2005 Chateau Systems, Inc.")
chateauExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 1))
if mibBuilder.loadTexts: chateauExperimental.setStatus('current')
if mibBuilder.loadTexts: chateauExperimental.setDescription('All experimental MIBs are organized under this node. When those MIBs have been fully developed and tested, they will be moved under the chateauRegistrations Node. MIBs which are in Beta-test status may also appear under this experimental node.')
chateauRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2))
if mibBuilder.loadTexts: chateauRegistrations.setStatus('current')
if mibBuilder.loadTexts: chateauRegistrations.setDescription('All MIBs (that have completed testing), along with associated registration data, are organized under this node. This includes Global Registrations, Product MIBs, and registration of MIBs in other categories.')
chateauGlobalRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 1))
if mibBuilder.loadTexts: chateauGlobalRegistrations.setStatus('current')
if mibBuilder.loadTexts: chateauGlobalRegistrations.setDescription('This node is intended for global registration information only. EG, OID definitions that register products.')
chateauProductRegs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 1, 1))
if mibBuilder.loadTexts: chateauProductRegs.setStatus('current')
if mibBuilder.loadTexts: chateauProductRegs.setDescription('Specific Product Registrations are under this node.')
chateauConsumerProductRegs = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 1, 1, 3))
if mibBuilder.loadTexts: chateauConsumerProductRegs.setStatus('current')
if mibBuilder.loadTexts: chateauConsumerProductRegs.setDescription('Consumer Product Registrations are under this node.')
chateauCDProductReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 1, 1, 3, 1))
if mibBuilder.loadTexts: chateauCDProductReg.setStatus('current')
if mibBuilder.loadTexts: chateauCDProductReg.setDescription('The OID of this node is the definition of the authoritative registration for the Chateau Systems CD Product.')
chateauProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 2))
if mibBuilder.loadTexts: chateauProducts.setStatus('current')
if mibBuilder.loadTexts: chateauProducts.setDescription('All Chateau Systems Product MIBs are organized under this node.')
chateauConsumerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 2, 3))
if mibBuilder.loadTexts: chateauConsumerProducts.setStatus('current')
if mibBuilder.loadTexts: chateauConsumerProducts.setDescription('All Chateau Systems Consumer Product MIBs are organized under this node')
chateauCDProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 10910, 2, 2, 3, 1))
if mibBuilder.loadTexts: chateauCDProduct.setStatus('current')
if mibBuilder.loadTexts: chateauCDProduct.setDescription('Chateau CD Product MIBs are organized under this node.')
class ChateauTrapControl(TextualConvention, Integer32):
    description = 'Used to enable or disable specific Traps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("trapEnable", 1), ("trapDisable", 2))

class ChateauEventSeverity(TextualConvention, Integer32):
    description = 'Used to assign severities to detected events. Event Severity data is sent with Traps, to indicate the severity of particular Traps. Spaces have been left in the enumerated definitions to any future severity definitions. For example: { normal(1), warning(2), minor(3), major(4), critical(5)}'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("major", 4))

mibBuilder.exportSymbols("CHATEAUSYSTEMS-REGISTRATIONS-MIB", PYSNMP_MODULE_ID=chateausystems, chateauProducts=chateauProducts, chateauGlobalRegistrations=chateauGlobalRegistrations, ChateauTrapControl=ChateauTrapControl, chateauRegistrations=chateauRegistrations, ChateauEventSeverity=ChateauEventSeverity, chateauCDProduct=chateauCDProduct, chateauProductRegs=chateauProductRegs, chateauConsumerProductRegs=chateauConsumerProductRegs, chateauExperimental=chateauExperimental, chateausystems=chateausystems, chateauCDProductReg=chateauCDProductReg, chateauConsumerProducts=chateauConsumerProducts)
