#
# PySNMP MIB module AT-EPSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-EPSR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, ModuleIdentity, ObjectIdentity, Counter64, Counter32, Unsigned32, Bits, IpAddress, MibIdentifier, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "ModuleIdentity", "ObjectIdentity", "Counter64", "Counter32", "Unsigned32", "Bits", "IpAddress", "MibIdentifier", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
epsr = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136))
epsr.setRevisions(('2006-11-22 12:12', '2006-02-16 16:19',))
if mibBuilder.loadTexts: epsr.setLastUpdated('200611221212Z')
if mibBuilder.loadTexts: epsr.setOrganization('Allied Telesis, Inc')
class EpsrNodeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("idle", 0), ("complete", 1), ("failed", 2), ("linksUp", 3), ("linksDown", 4), ("preForward", 5), ("unknown", 6))

class EpsrInterfaceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("blocked", 1), ("forward", 2))

epsrEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 1))
epsrNodeTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 1, 1)).setObjects(("AT-EPSR-MIB", "epsrNodeTrapType"), ("AT-EPSR-MIB", "epsrDomainName"), ("AT-EPSR-MIB", "epsrFromState"), ("AT-EPSR-MIB", "epsrToState"), ("AT-EPSR-MIB", "epsrControlVlanId"), ("AT-EPSR-MIB", "epsrPrimaryIfIndex"), ("AT-EPSR-MIB", "epsrPrimaryIfState"), ("AT-EPSR-MIB", "epsrSecondaryIfIndex"), ("AT-EPSR-MIB", "epsrSecondaryIfState"))
if mibBuilder.loadTexts: epsrNodeTrap.setStatus('current')
epsrEventVariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2), )
if mibBuilder.loadTexts: epsrEventVariablesTable.setStatus('current')
epsrEventVariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1), ).setIndexNames((0, "AT-EPSR-MIB", "epsrDomainName"))
if mibBuilder.loadTexts: epsrEventVariablesEntry.setStatus('current')
epsrNodeTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("masterNodeTrap", 1), ("transitNodeTrap", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrNodeTrapType.setStatus('current')
epsrDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 2), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrDomainName.setStatus('current')
epsrFromState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 3), EpsrNodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrFromState.setStatus('current')
epsrToState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 4), EpsrNodeState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrToState.setStatus('current')
epsrControlVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrControlVlanId.setStatus('current')
epsrPrimaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrPrimaryIfIndex.setStatus('current')
epsrPrimaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 7), EpsrInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrPrimaryIfState.setStatus('current')
epsrSecondaryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 8), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrSecondaryIfIndex.setStatus('current')
epsrSecondaryIfState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 136, 2, 1, 9), EpsrInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: epsrSecondaryIfState.setStatus('current')
mibBuilder.exportSymbols("AT-EPSR-MIB", epsrSecondaryIfState=epsrSecondaryIfState, epsrToState=epsrToState, epsrNodeTrap=epsrNodeTrap, epsrControlVlanId=epsrControlVlanId, epsrEventVariablesTable=epsrEventVariablesTable, PYSNMP_MODULE_ID=epsr, EpsrInterfaceState=EpsrInterfaceState, EpsrNodeState=EpsrNodeState, epsrFromState=epsrFromState, epsrEvents=epsrEvents, epsrNodeTrapType=epsrNodeTrapType, epsrPrimaryIfState=epsrPrimaryIfState, epsrSecondaryIfIndex=epsrSecondaryIfIndex, epsrDomainName=epsrDomainName, epsrPrimaryIfIndex=epsrPrimaryIfIndex, epsrEventVariablesEntry=epsrEventVariablesEntry, epsr=epsr)
