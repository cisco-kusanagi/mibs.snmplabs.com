#
# PySNMP MIB module BIANCA-ETH-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-ETH-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Bits, Counter32, IpAddress, ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, iso, Unsigned32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Bits", "Counter32", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "iso", "Unsigned32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier")
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
if mibBuilder.loadTexts: ethIfTable.setDescription('The ethIfTable allows to perform interface status changes of one or more interfaces based on a status transition of another interface.')
ethIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1), ).setIndexNames((0, "BIANCA-ETH-IF-MIB", "ethIfIndex"))
if mibBuilder.loadTexts: ethIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ethIfEntry.setDescription('')
ethIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ethIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ethIfIndex.setDescription('A unique value for each interface. Its value ranges between 1000 and the value of ifNumber. The following information is encoded in the ifIndex: a. An ifIndex between 1000 and 9999 define hardware interfaces with the following attributes. b. An ifIndex greater than or equal to 10000 defines a software interface. Examples include the dialup-interfaces as defined in the biboPPPTable.')
ethIfPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfPortGroup.setStatus('mandatory')
if mibBuilder.loadTexts: ethIfPortGroup.setDescription('The port group the interface is member of.')
ethIfMACSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfMACSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ethIfMACSlot.setDescription('The slot of the connected media access controller.')
ethIfMACUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfMACUnit.setStatus('mandatory')
if mibBuilder.loadTexts: ethIfMACUnit.setDescription('The unit of the connected media access controller.')
ethIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ethIfAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ethIfAdminStatus.setDescription('')
mibBuilder.exportSymbols("BIANCA-ETH-IF-MIB", ethIfIndex=ethIfIndex, ethIfPortGroup=ethIfPortGroup, Date=Date, ethIfAdminStatus=ethIfAdminStatus, HexValue=HexValue, ethIfMACSlot=ethIfMACSlot, ethIfMACUnit=ethIfMACUnit, ethIfTable=ethIfTable, PhysAddress=PhysAddress, bintec=bintec, eth=eth, bibo=bibo, ethIfEntry=ethIfEntry)
