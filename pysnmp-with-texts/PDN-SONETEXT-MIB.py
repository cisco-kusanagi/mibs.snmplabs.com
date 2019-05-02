#
# PySNMP MIB module PDN-SONETEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-SONETEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
pdnSonetMIB, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnSonetMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, iso, Gauge32, ObjectIdentity, Bits, Counter32, TimeTicks, IpAddress, Unsigned32, NotificationType, MibIdentifier, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "iso", "Gauge32", "ObjectIdentity", "Bits", "Counter32", "TimeTicks", "IpAddress", "Unsigned32", "NotificationType", "MibIdentifier", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonetPathCurrentStatus, sonetLineCurrentStatus, sonetSectionCurrentStatus = mibBuilder.importSymbols("SONET-MIB", "sonetPathCurrentStatus", "sonetLineCurrentStatus", "sonetSectionCurrentStatus")
devSonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1))
devSonetTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 2))
devSonetConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1), )
if mibBuilder.loadTexts: devSonetConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: devSonetConfigTable.setDescription('The Paradyne Sonet-MIB Table Augment.')
devSonetConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1), ).setIndexNames((0, "PDN-SONETEXT-MIB", "devSonetIfIndex"))
if mibBuilder.loadTexts: devSonetConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devSonetConfigEntry.setDescription('An entry in the Paradyne Sonet-MIB Interface Config Table.')
devSonetIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSonetIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: devSonetIfIndex.setDescription('The index value which uniquely identifies the interface for which this entry contains information on interface tests. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex from the Interfaces table of MIB II (RFC 1213).')
devSonetXmitClkSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devSonetXmitClkSrc.setStatus('mandatory')
if mibBuilder.loadTexts: devSonetXmitClkSrc.setDescription('This object is used to configure the clock to be used by the transmit side of the interface.')
devSonetStatusLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devSonetStatusLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: devSonetStatusLastChange.setDescription("The value of MIB II's sysUpTime object at the time this Sonet entered its current line status state. If the current state was entered prior to the last re-initialization of the proxy-agent, then this object contains a zero value.")
devSonetStatusChangeTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devSonetStatusChangeTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: devSonetStatusChangeTrapEnable.setDescription('Indicates whether devSonetStatusChange traps should be generated for this interface.')
devSonetStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 13, 2) + (0,1)).setObjects(("PDN-SONETEXT-MIB", "devSonetStatusLastChange"), ("SONET-MIB", "sonetSectionCurrentStatus"), ("SONET-MIB", "sonetLineCurrentStatus"), ("SONET-MIB", "sonetPathCurrentStatus"))
if mibBuilder.loadTexts: devSonetStatusChange.setDescription('A devSonetStatusChange trap is sent when the value of an instance of sonetSectionCurrentStatus or sonetLineCurrentStatus or sonetPathCurrentStatus changes. It can be utilized by an NMS to trigger polls. When the line status change results in a lower level line status change (i.e. sonet), then no traps for the lower level are sent.')
mibBuilder.exportSymbols("PDN-SONETEXT-MIB", devSonetStatusChange=devSonetStatusChange, devSonetIfIndex=devSonetIfIndex, devSonetConfigTable=devSonetConfigTable, devSonetStatusLastChange=devSonetStatusLastChange, devSonetTraps=devSonetTraps, devSonetStatusChangeTrapEnable=devSonetStatusChangeTrapEnable, devSonetConfigEntry=devSonetConfigEntry, devSonetConfig=devSonetConfig, devSonetXmitClkSrc=devSonetXmitClkSrc)
