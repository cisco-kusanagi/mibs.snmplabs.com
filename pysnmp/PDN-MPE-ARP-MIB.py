#
# PySNMP MIB module PDN-MPE-ARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-ARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_arp, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-arp")
SwitchState, VnidRange = mibBuilder.importSymbols("PDN-TC", "SwitchState", "VnidRange")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, ModuleIdentity, MibIdentifier, Unsigned32, ObjectIdentity, Integer32, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "ModuleIdentity", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Integer32", "Bits", "Counter32")
RowStatus, TextualConvention, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "DisplayString", "TruthValue")
class Bit32(Integer32):
    pass

mpePdnNetToMediaGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1))
mpePdnNetToMediaMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 2))
mpePdnNetTo8023MediaParams = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1))
mpePdnNetTo8023MediaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 2))
mpePdnNetTo8023MediaParamsTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1), )
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsTable.setStatus('mandatory')
mpePdnNetTo8023MediaParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsEntry.setStatus('mandatory')
mpePdnNetTo8023MediaParamsCompEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 1), Integer32().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsCompEntryTimeout.setStatus('mandatory')
mpePdnNetTo8023MediaParamsIncompEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 2), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsIncompEntryTimeout.setStatus('mandatory')
mpePdnNetTo8023MediaParamsDefRouteEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsDefRouteEntryTimeout.setStatus('mandatory')
mibBuilder.exportSymbols("PDN-MPE-ARP-MIB", mpePdnNetTo8023MediaParams=mpePdnNetTo8023MediaParams, Bit32=Bit32, mpePdnNetTo8023MediaParamsDefRouteEntryTimeout=mpePdnNetTo8023MediaParamsDefRouteEntryTimeout, mpePdnNetTo8023MediaParamsCompEntryTimeout=mpePdnNetTo8023MediaParamsCompEntryTimeout, mpePdnNetTo8023MediaParamsIncompEntryTimeout=mpePdnNetTo8023MediaParamsIncompEntryTimeout, mpePdnNetToMediaMIBTraps=mpePdnNetToMediaMIBTraps, mpePdnNetTo8023MediaParamsEntry=mpePdnNetTo8023MediaParamsEntry, mpePdnNetTo8023MediaConfig=mpePdnNetTo8023MediaConfig, mpePdnNetTo8023MediaParamsTable=mpePdnNetTo8023MediaParamsTable, mpePdnNetToMediaGenericMIBObjects=mpePdnNetToMediaGenericMIBObjects)
