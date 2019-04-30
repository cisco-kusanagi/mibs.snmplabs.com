#
# PySNMP MIB module BRIDGEEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BRIDGEEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:23:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
bridgeExt, = mibBuilder.importSymbols("APENT-MIB", "bridgeExt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, ObjectIdentity, Unsigned32, ModuleIdentity, TimeTicks, Counter64, IpAddress, NotificationType, Gauge32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter64", "IpAddress", "NotificationType", "Gauge32", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Timeout(Integer32):
    pass

apBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1))
apBridgeMaxAge = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 1), Timeout().subtype(subtypeSpec=ValueRangeConstraint(6, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgeMaxAge.setStatus('mandatory')
apBridgeHelloTime = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 2), Timeout().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgeHelloTime.setStatus('mandatory')
apBridgeForwardDelay = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 3), Timeout().subtype(subtypeSpec=ValueRangeConstraint(4, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgeForwardDelay.setStatus('mandatory')
apBridgePortTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4), )
if mibBuilder.loadTexts: apBridgePortTable.setStatus('mandatory')
apBridgePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1), ).setIndexNames((0, "BRIDGEEXT-MIB", "apBridgePort"))
if mibBuilder.loadTexts: apBridgePortEntry.setStatus('mandatory')
apBridgePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apBridgePort.setStatus('mandatory')
apBridgePortVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgePortVlan.setStatus('mandatory')
apBridgeSpanningTreeState = MibScalar((1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apBridgeSpanningTreeState.setStatus('mandatory')
mibBuilder.exportSymbols("BRIDGEEXT-MIB", apBridgePortVlan=apBridgePortVlan, apBridgeForwardDelay=apBridgeForwardDelay, apBridgePortTable=apBridgePortTable, apBridgeSpanningTreeState=apBridgeSpanningTreeState, apBridge=apBridge, apBridgePortEntry=apBridgePortEntry, apBridgeHelloTime=apBridgeHelloTime, apBridgePort=apBridgePort, apBridgeMaxAge=apBridgeMaxAge, Timeout=Timeout)
