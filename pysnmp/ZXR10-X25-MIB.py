#
# PySNMP MIB module ZXR10-X25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-X25-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Counter32, TimeTicks, IpAddress, NotificationType, iso, enterprises, Unsigned32, Bits, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, mgmt, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Counter32", "TimeTicks", "IpAddress", "NotificationType", "iso", "enterprises", "Unsigned32", "Bits", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "mgmt", "Counter64")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10X25 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 4000))
class DisplayString(OctetString):
    pass

zxr10X25OprTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1), )
if mibBuilder.loadTexts: zxr10X25OprTable.setStatus('current')
zxr10X25OprEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zxr10X25OprEntry.setStatus('current')
zxr10X25OprXconnenctIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprXconnenctIfName.setStatus('current')
zxr10X25OprLocalswitchIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprLocalswitchIfName.setStatus('current')
zxr10X25OprDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprDLCI.setStatus('current')
zxr10X25OprType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("localswitch", 1), ("xconnect", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprType.setStatus('current')
zxr10X25OprStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprStatus.setStatus('current')
mibBuilder.exportSymbols("ZXR10-X25-MIB", zte=zte, zxr10=zxr10, zxr10X25OprType=zxr10X25OprType, zxr10X25OprLocalswitchIfName=zxr10X25OprLocalswitchIfName, DisplayString=DisplayString, zxr10X25OprStatus=zxr10X25OprStatus, zxr10X25=zxr10X25, zxr10X25OprTable=zxr10X25OprTable, zxr10X25OprEntry=zxr10X25OprEntry, zxr10X25OprXconnenctIfName=zxr10X25OprXconnenctIfName, zxr10X25OprDLCI=zxr10X25OprDLCI)
