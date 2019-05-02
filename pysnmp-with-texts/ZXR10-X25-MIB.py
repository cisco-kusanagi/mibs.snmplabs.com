#
# PySNMP MIB module ZXR10-X25-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-X25-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, ModuleIdentity, Integer32, TimeTicks, NotificationType, Unsigned32, Gauge32, ObjectIdentity, IpAddress, NotificationType, Bits, Counter64, iso, mgmt, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "ModuleIdentity", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "Gauge32", "ObjectIdentity", "IpAddress", "NotificationType", "Bits", "Counter64", "iso", "mgmt", "enterprises")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10X25 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 4000))
class DisplayString(OctetString):
    pass

zxr10X25OprTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1), )
if mibBuilder.loadTexts: zxr10X25OprTable.setStatus('current')
if mibBuilder.loadTexts: zxr10X25OprTable.setDescription('X.25 operation table')
zxr10X25OprEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: zxr10X25OprEntry.setStatus('current')
if mibBuilder.loadTexts: zxr10X25OprEntry.setDescription('X.25 operation table entry')
zxr10X25OprXconnenctIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprXconnenctIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10X25OprXconnenctIfName.setDescription('X.25 entry -> X.25 xconnect interface DLCI')
zxr10X25OprLocalswitchIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprLocalswitchIfName.setStatus('current')
if mibBuilder.loadTexts: zxr10X25OprLocalswitchIfName.setDescription('X.25 entry -> X.25 interface')
zxr10X25OprDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprDLCI.setStatus('current')
if mibBuilder.loadTexts: zxr10X25OprDLCI.setDescription('X.25 DLCI size : from 16 to 1007')
zxr10X25OprType = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("localswitch", 1), ("xconnect", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprType.setStatus('current')
if mibBuilder.loadTexts: zxr10X25OprType.setDescription('')
zxr10X25OprStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 4000, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxr10X25OprStatus.setStatus('current')
if mibBuilder.loadTexts: zxr10X25OprStatus.setDescription("The status of this conceptual row. To create a row in this table, a manager must set this object to createAndGo(4) Until instances of all corresponding columns are appropriately configured, the value of the corresponding instance of the zxr10X25OprStatus column is 'notReady'")
mibBuilder.exportSymbols("ZXR10-X25-MIB", zte=zte, zxr10X25OprXconnenctIfName=zxr10X25OprXconnenctIfName, zxr10X25OprTable=zxr10X25OprTable, zxr10X25=zxr10X25, zxr10X25OprLocalswitchIfName=zxr10X25OprLocalswitchIfName, zxr10X25OprDLCI=zxr10X25OprDLCI, zxr10=zxr10, zxr10X25OprEntry=zxr10X25OprEntry, zxr10X25OprType=zxr10X25OprType, DisplayString=DisplayString, zxr10X25OprStatus=zxr10X25OprStatus)
