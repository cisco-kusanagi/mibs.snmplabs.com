#
# PySNMP MIB module CT-DAREGISTRY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-DAREGISTRY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:28:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, ObjectIdentity, MibIdentifier, Counter64, iso, Counter32, NotificationType, Unsigned32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "ObjectIdentity", "MibIdentifier", "Counter64", "iso", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
class DisplayString(OctetString):
    pass

ctDARegistryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 1), )
if mibBuilder.loadTexts: ctDARegistryTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctDARegistryTable.setDescription('A list of Demand Access WAN firmware components.')
ctDARegistryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1), ).setIndexNames((0, "CT-DAREGISTRY-MIB", "ctDARegistryIndex"), (0, "CT-DAREGISTRY-MIB", "ctDARegistryInstance"))
if mibBuilder.loadTexts: ctDARegistryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctDARegistryEntry.setDescription('An entry containing management information applicable to a particular subsystem.')
ctDARegistryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctDARegistryIndex.setDescription('This is the category for this object.')
ctDARegistryInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryInstance.setStatus('mandatory')
if mibBuilder.loadTexts: ctDARegistryInstance.setDescription('This is a unique instance within the category for this object.')
ctDARegistryAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDARegistryAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDARegistryAdminStatus.setDescription('The desired state of the subsystem. The testing(3) state indicates that no operational functions can be passed. When a managed system initializes, all subsystems start with ctDARegistryAdminStatus in the up(1) state. As a result of either explicit management action or per configuration information retained by the managed system, ctDARegistryAdminStatus is then changed to either the dowm(2) or testing(3) states (or remains in the up(1) state).')
ctDARegistryOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDARegistryOperStatus.setDescription('The mandatory operational state of the subsystem. The testing(3) state indicates that no operational functions can be passed. If ctDARegistryAdminStatus is down(2) then ctDARegistryOperStatus should be down(2). If ctDARegistryAdminStatus is changed to up(1) then ctDARegistryOperStatus should change to up(1) if the subsystem is ready to function; it should change to dormant(5) if the subsystem is waiting for external actions; it should remain in the down(2) state if and only if there is a fault that prevents if from going to the up(1) state. The notPresent state is a refinement on the down state which indicates that the relevant interface is down specifically because some component (typically, a hardware component) is not present in the managed system. The lowerLayerDown state is also a refinement on the down state. This new state indicates that this system runs on top of one or more interfaces (see ifStackTable) and that this system is down specifically because one or more of these lower-layer interfaces are down. ')
ctDARegistryLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: ctDARegistryLastChange.setDescription('The value of sysUpTime at the time the subsystem entered its mandatory operational state. If the mandatory state was entered prior to the last re-initialization of the local network management subsystem, then this object contains a zero value.')
ctDARegistryDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDARegistryDescr.setStatus('mandatory')
if mibBuilder.loadTexts: ctDARegistryDescr.setDescription('A textual string that identifies the subsystem.')
mibBuilder.exportSymbols("CT-DAREGISTRY-MIB", ctDARegistryLastChange=ctDARegistryLastChange, DisplayString=DisplayString, ctDARegistryIndex=ctDARegistryIndex, ctDARegistryEntry=ctDARegistryEntry, ctDARegistryOperStatus=ctDARegistryOperStatus, ctDARegistryDescr=ctDARegistryDescr, ctDARegistryTable=ctDARegistryTable, ctSSA=ctSSA, ctDARegistryInstance=ctDARegistryInstance, ctDARegistryAdminStatus=ctDARegistryAdminStatus)
