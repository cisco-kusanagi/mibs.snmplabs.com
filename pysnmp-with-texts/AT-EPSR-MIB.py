#
# PySNMP MIB module AT-EPSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-EPSR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, TimeTicks, MibIdentifier, iso, IpAddress, ModuleIdentity, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "TimeTicks", "MibIdentifier", "iso", "IpAddress", "ModuleIdentity", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
epsr = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136))
epsr.setRevisions(('2006-11-22 12:12', '2006-02-16 16:19',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: epsr.setRevisionsDescriptions(('This MIB file contains definitions of managed objects for the code module responsible for handling EPSR on Allied Telesis switches.', 'Initial Revision',))
if mibBuilder.loadTexts: epsr.setLastUpdated('200611221212Z')
if mibBuilder.loadTexts: epsr.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: epsr.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: epsr.setDescription('Convert epsrEventVariables into a table entry, so variable of mutiple EPSR domains can be obtained.')
class EpsrNodeState(TextualConvention, Integer32):
    description = 'Defines the node states that can be passed around in EPSR Node Traps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 0), ("complete", 1), ("failed", 2), ("linksUp", 3), ("linksDown", 4), ("preForward", 5), ("unknown", 6))

class EpsrInterfaceState(TextualConvention, Integer32):
    description = 'Defines the interface states that can be passed around in EPSR Node Traps.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("blocked", 1), ("forward", 2))

epsrEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 1))
epsrNodeTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 1, 1)).setObjects(("AT-EPSR-MIB", "epsrNodeTrapType"), ("AT-EPSR-MIB", "epsrDomainName"), ("AT-EPSR-MIB", "epsrFromState"), ("AT-EPSR-MIB", "epsrToState"), ("AT-EPSR-MIB", "epsrControlVlanId"), ("AT-EPSR-MIB", "epsrPrimaryIfIndex"), ("AT-EPSR-MIB", "epsrPrimaryIfState"), ("AT-EPSR-MIB", "epsrSecondaryIfIndex"), ("AT-EPSR-MIB", "epsrSecondaryIfState"))
if mibBuilder.loadTexts: epsrNodeTrap.setStatus('current')
if mibBuilder.loadTexts: epsrNodeTrap.setDescription('EPSR Master/Transit node state transition trap.')
epsrEventVariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2), )
if mibBuilder.loadTexts: epsrEventVariablesTable.setStatus('current')
if mibBuilder.loadTexts: epsrEventVariablesTable.setDescription('This table contains rows of epsrEventVariablesEntry.')
epsrEventVariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1), ).setIndexNames((0, "AT-EPSR-MIB", "epsrDomainName"))
if mibBuilder.loadTexts: epsrEventVariablesEntry.setStatus('current')
if mibBuilder.loadTexts: epsrEventVariablesEntry.setDescription('An entry in the ATL enterprise epsrEventVariablesTable.')
epsrNodeTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("masterNodeTrap", 1), ("transitNodeTrap", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrNodeTrapType.setStatus('current')
if mibBuilder.loadTexts: epsrNodeTrapType.setDescription('This is the trap type of the EPSR node trap (master/transit).')
epsrDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 2), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrDomainName.setStatus('current')
if mibBuilder.loadTexts: epsrDomainName.setDescription('Assigned name of the EPSR domain.')
epsrFromState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 3), EpsrNodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrFromState.setStatus('current')
if mibBuilder.loadTexts: epsrFromState.setDescription('Defined state that an EPSR domain is transitioning from.')
epsrToState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 4), EpsrNodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrToState.setStatus('current')
if mibBuilder.loadTexts: epsrToState.setDescription('Defined state that an EPSR domain is transitioning to.')
epsrControlVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrControlVlanId.setStatus('current')
if mibBuilder.loadTexts: epsrControlVlanId.setDescription('VLAN identifier for the control VLAN.')
epsrPrimaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrPrimaryIfIndex.setStatus('current')
if mibBuilder.loadTexts: epsrPrimaryIfIndex.setDescription('IfIndex of the primary interface.')
epsrPrimaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 7), EpsrInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrPrimaryIfState.setStatus('current')
if mibBuilder.loadTexts: epsrPrimaryIfState.setDescription('Defined current state of the primary interface.')
epsrSecondaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 8), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrSecondaryIfIndex.setStatus('current')
if mibBuilder.loadTexts: epsrSecondaryIfIndex.setDescription('IfIndex of the secondary interface.')
epsrSecondaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 9), EpsrInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrSecondaryIfState.setStatus('current')
if mibBuilder.loadTexts: epsrSecondaryIfState.setDescription('Defined current state of the secondary interface.')
mibBuilder.exportSymbols("AT-EPSR-MIB", epsrDomainName=epsrDomainName, epsrSecondaryIfIndex=epsrSecondaryIfIndex, epsrToState=epsrToState, PYSNMP_MODULE_ID=epsr, epsrEventVariablesTable=epsrEventVariablesTable, epsr=epsr, epsrEventVariablesEntry=epsrEventVariablesEntry, epsrFromState=epsrFromState, EpsrNodeState=EpsrNodeState, epsrEvents=epsrEvents, epsrNodeTrap=epsrNodeTrap, epsrSecondaryIfState=epsrSecondaryIfState, epsrPrimaryIfIndex=epsrPrimaryIfIndex, EpsrInterfaceState=EpsrInterfaceState, epsrControlVlanId=epsrControlVlanId, epsrPrimaryIfState=epsrPrimaryIfState, epsrNodeTrapType=epsrNodeTrapType)
