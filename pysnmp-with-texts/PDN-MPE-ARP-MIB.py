#
# PySNMP MIB module PDN-MPE-ARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-MPE-ARP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
mpe_arp, = mibBuilder.importSymbols("PDN-HEADER-MIB", "mpe-arp")
SwitchState, VnidRange = mibBuilder.importSymbols("PDN-TC", "SwitchState", "VnidRange")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, iso, IpAddress, NotificationType, Gauge32, Integer32, TimeTicks, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "iso", "IpAddress", "NotificationType", "Gauge32", "Integer32", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "Bits")
DisplayString, TextualConvention, MacAddress, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress", "TruthValue", "RowStatus")
class Bit32(Integer32):
    pass

mpePdnNetToMediaGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1))
mpePdnNetToMediaMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 2))
mpePdnNetTo8023MediaParams = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1))
mpePdnNetTo8023MediaConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 2))
mpePdnNetTo8023MediaParamsTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1), )
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsTable.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsTable.setDescription('A table that contains ARP Parameters configuration information .')
mpePdnNetTo8023MediaParamsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsEntry.setDescription('A list of information about ARP Parameters.')
mpePdnNetTo8023MediaParamsCompEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 1), Integer32().clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsCompEntryTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsCompEntryTimeout.setDescription(' Complete Entry Timeout is the length of time that a complete entry remains in the ARP table before removal. A complete entry is one for which there is a MAC address -- i.e. a node has responded to the ARP request. If an entry gets this old without being referenced, it will be removed from the table. The range for this parameter is 1 to 200000 minutes.')
mpePdnNetTo8023MediaParamsIncompEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 2), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsIncompEntryTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsIncompEntryTimeout.setDescription(' Incomplete Entry Timeout is the length of time that an incomplete entry remains in the ARP table before removal. An incomplete entry is one for which there is no MAC address -- i.e. an ARP request has been made, but no response has been received. This is also the amount of time that a packet will remain in the system while waiting for address resolution. The range for this parameter is 1 to 255 minutes.')
mpePdnNetTo8023MediaParamsDefRouteEntryTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 3), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsDefRouteEntryTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: mpePdnNetTo8023MediaParamsDefRouteEntryTimeout.setDescription('Default Route Entry Timeout is the length of time a default route entry will remain in the ARP table. If default route gets this old without being referenced, an ARP request will be sent to the next hop router. If no response is received, it will be removed from the ARP table and the card will switch to the next reachable default route with the highest preference. The range for this parameter is 1 to 20 minutes.')
mibBuilder.exportSymbols("PDN-MPE-ARP-MIB", mpePdnNetTo8023MediaConfig=mpePdnNetTo8023MediaConfig, mpePdnNetToMediaMIBTraps=mpePdnNetToMediaMIBTraps, mpePdnNetTo8023MediaParamsCompEntryTimeout=mpePdnNetTo8023MediaParamsCompEntryTimeout, mpePdnNetTo8023MediaParams=mpePdnNetTo8023MediaParams, mpePdnNetTo8023MediaParamsTable=mpePdnNetTo8023MediaParamsTable, Bit32=Bit32, mpePdnNetToMediaGenericMIBObjects=mpePdnNetToMediaGenericMIBObjects, mpePdnNetTo8023MediaParamsEntry=mpePdnNetTo8023MediaParamsEntry, mpePdnNetTo8023MediaParamsIncompEntryTimeout=mpePdnNetTo8023MediaParamsIncompEntryTimeout, mpePdnNetTo8023MediaParamsDefRouteEntryTimeout=mpePdnNetTo8023MediaParamsDefRouteEntryTimeout)
