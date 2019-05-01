#
# PySNMP MIB module NWSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NWSD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ipAddrEntry, = mibBuilder.importSymbols("IP-MIB", "ipAddrEntry")
rsNWSD, = mibBuilder.importSymbols("RADWARE-MIB", "rsNWSD")
rndErrorDesc, rndErrorSeverity, rsServerDispatcher = mibBuilder.importSymbols("RND-MIB", "rndErrorDesc", "rndErrorSeverity", "rsServerDispatcher")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, ModuleIdentity, TimeTicks, NotificationType, Bits, MibIdentifier, enterprises, Integer32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "Bits", "MibIdentifier", "enterprises", "Integer32", "Counter64", "Unsigned32")
TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString")
class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

rsNWSDProximity = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1))
rsWSDProximityHopsWeight = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDProximityHopsWeight.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDProximityHopsWeight.setDescription('The weight given to the clients hops distance in the dispatching decision')
rsWSDProximityLatencyWeight = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDProximityLatencyWeight.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDProximityLatencyWeight.setDescription('The weight given to the clients latency in the dispatching decision')
rsWSDProximityLoadWeight = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDProximityLoadWeight.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDProximityLoadWeight.setDescription('The weight given to the site load in the dispatching decision')
rsWSDDNSttl = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDDNSttl.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDDNSttl.setDescription('TTL for DNS replies.')
rsWSDURLSuperFarmTable = MibTable((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3), )
if mibBuilder.loadTexts: rsWSDURLSuperFarmTable.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDURLSuperFarmTable.setDescription('A table for managing the farm decision according to the incoming URL.')
rsWSDURLSuperFarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1), ).setIndexNames((0, "NWSD-MIB", "rsWSDURL"))
if mibBuilder.loadTexts: rsWSDURLSuperFarmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDURLSuperFarmEntry.setDescription(' The row definition for this table.')
rsWSDURLFarmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDURLFarmAddress.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDURLFarmAddress.setDescription('IP address of the farm to use with the URL.')
rsWSDURL = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDURL.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDURL.setDescription('The URL representing the farm.')
rsWSDURLStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDURLStatus.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDURLStatus.setDescription('Row status for the URL.')
rsWSDClientGroupingMask = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 26), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDClientGroupingMask.setStatus('mandatory')
if mibBuilder.loadTexts: rsWSDClientGroupingMask.setDescription('Client IP address mask.')
mibBuilder.exportSymbols("NWSD-MIB", RowStatus=RowStatus, rsWSDURLStatus=rsWSDURLStatus, rsWSDDNSttl=rsWSDDNSttl, rsNWSDProximity=rsNWSDProximity, rsWSDURLSuperFarmTable=rsWSDURLSuperFarmTable, rsWSDProximityHopsWeight=rsWSDProximityHopsWeight, rsWSDURLSuperFarmEntry=rsWSDURLSuperFarmEntry, rsWSDProximityLatencyWeight=rsWSDProximityLatencyWeight, rsWSDProximityLoadWeight=rsWSDProximityLoadWeight, NetNumber=NetNumber, rsWSDClientGroupingMask=rsWSDClientGroupingMask, rsWSDURLFarmAddress=rsWSDURLFarmAddress, rsWSDURL=rsWSDURL, TruthValue=TruthValue)
