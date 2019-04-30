#
# PySNMP MIB module NWSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NWSD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ipAddrEntry, = mibBuilder.importSymbols("IP-MIB", "ipAddrEntry")
rsNWSD, = mibBuilder.importSymbols("RADWARE-MIB", "rsNWSD")
rndErrorDesc, rsServerDispatcher, rndErrorSeverity = mibBuilder.importSymbols("RND-MIB", "rndErrorDesc", "rsServerDispatcher", "rndErrorSeverity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, TimeTicks, Bits, NotificationType, IpAddress, Integer32, iso, ObjectIdentity, enterprises, MibIdentifier, ModuleIdentity, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "TimeTicks", "Bits", "NotificationType", "IpAddress", "Integer32", "iso", "ObjectIdentity", "enterprises", "MibIdentifier", "ModuleIdentity", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
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
rsWSDProximityLatencyWeight = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDProximityLatencyWeight.setStatus('mandatory')
rsWSDProximityLoadWeight = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDProximityLoadWeight.setStatus('mandatory')
rsWSDDNSttl = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDDNSttl.setStatus('mandatory')
rsWSDURLSuperFarmTable = MibTable((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3), )
if mibBuilder.loadTexts: rsWSDURLSuperFarmTable.setStatus('mandatory')
rsWSDURLSuperFarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1), ).setIndexNames((0, "NWSD-MIB", "rsWSDURL"))
if mibBuilder.loadTexts: rsWSDURLSuperFarmEntry.setStatus('mandatory')
rsWSDURLFarmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDURLFarmAddress.setStatus('mandatory')
rsWSDURL = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDURL.setStatus('mandatory')
rsWSDURLStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDURLStatus.setStatus('mandatory')
rsWSDClientGroupingMask = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 1, 40, 26), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rsWSDClientGroupingMask.setStatus('mandatory')
mibBuilder.exportSymbols("NWSD-MIB", RowStatus=RowStatus, rsWSDProximityLatencyWeight=rsWSDProximityLatencyWeight, rsWSDProximityLoadWeight=rsWSDProximityLoadWeight, rsWSDProximityHopsWeight=rsWSDProximityHopsWeight, NetNumber=NetNumber, rsWSDURL=rsWSDURL, rsWSDDNSttl=rsWSDDNSttl, rsWSDURLStatus=rsWSDURLStatus, TruthValue=TruthValue, rsWSDURLSuperFarmEntry=rsWSDURLSuperFarmEntry, rsWSDClientGroupingMask=rsWSDClientGroupingMask, rsWSDURLFarmAddress=rsWSDURLFarmAddress, rsWSDURLSuperFarmTable=rsWSDURLSuperFarmTable, rsNWSDProximity=rsNWSDProximity)
