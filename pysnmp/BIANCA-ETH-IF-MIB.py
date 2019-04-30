#
# PySNMP MIB module BIANCA-ETH-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-ETH-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:21:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Unsigned32, Gauge32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, Counter64, IpAddress, TimeTicks, ModuleIdentity, enterprises, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Unsigned32", "Gauge32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "Counter64", "IpAddress", "TimeTicks", "ModuleIdentity", "enterprises", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
eth = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 37))
class Date(Integer32):
    pass

class HexValue(Integer32):
    pass

class PhysAddress(OctetString):
    pass

ethIfTable = MibTable((1, 3, 6, 1, 4, 1, 272, 4, 37, 1), )
if mibBuilder.loadTexts: ethIfTable.setStatus('mandatory')
ethIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1), ).setIndexNames((0, "BIANCA-ETH-IF-MIB", "ethIfIndex"))
if mibBuilder.loadTexts: ethIfEntry.setStatus('mandatory')
ethIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIfIndex.setStatus('mandatory')
ethIfPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfPortGroup.setStatus('mandatory')
ethIfMACSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfMACSlot.setStatus('mandatory')
ethIfMACUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfMACUnit.setStatus('mandatory')
ethIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfAdminStatus.setStatus('mandatory')
mibBuilder.exportSymbols("BIANCA-ETH-IF-MIB", ethIfMACUnit=ethIfMACUnit, PhysAddress=PhysAddress, ethIfEntry=ethIfEntry, bibo=bibo, eth=eth, HexValue=HexValue, ethIfAdminStatus=ethIfAdminStatus, Date=Date, ethIfIndex=ethIfIndex, ethIfTable=ethIfTable, ethIfMACSlot=ethIfMACSlot, ethIfPortGroup=ethIfPortGroup, bintec=bintec)
