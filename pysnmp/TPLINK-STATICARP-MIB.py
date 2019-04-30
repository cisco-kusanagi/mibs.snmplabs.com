#
# PySNMP MIB module TPLINK-STATICARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-STATICARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, Bits, ObjectIdentity, iso, NotificationType, Counter32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Bits", "ObjectIdentity", "iso", "NotificationType", "Counter32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkStaticARPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 54))
tplinkStaticARPMIB.setRevisions(('2014-11-24 14:42',))
if mibBuilder.loadTexts: tplinkStaticARPMIB.setLastUpdated('201411241442Z')
if mibBuilder.loadTexts: tplinkStaticARPMIB.setOrganization('TPLINK')
tplinkStaticARPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1))
tplinkStaticARPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 2))
tpStaticARPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1))
tpStaticARPConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1), )
if mibBuilder.loadTexts: tpStaticARPConfigTable.setStatus('current')
tpStaticARPConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-STATICARP-MIB", "tpStaticARPItemIp"))
if mibBuilder.loadTexts: tpStaticARPConfigEntry.setStatus('current')
tpStaticARPItemIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticARPItemIp.setStatus('current')
tpStaticARPItemMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticARPItemMac.setStatus('current')
tpStaticArpItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticArpItemInterfaceName.setStatus('current')
tpStaticARPItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 4), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticARPItemStatus.setStatus('current')
mibBuilder.exportSymbols("TPLINK-STATICARP-MIB", tpStaticARPConfig=tpStaticARPConfig, MacAddress=MacAddress, tpStaticARPItemIp=tpStaticARPItemIp, tpStaticARPItemStatus=tpStaticARPItemStatus, tplinkStaticARPMIBObjects=tplinkStaticARPMIBObjects, tpStaticARPConfigEntry=tpStaticARPConfigEntry, tplinkStaticARPNotifications=tplinkStaticARPNotifications, tpStaticArpItemInterfaceName=tpStaticArpItemInterfaceName, PYSNMP_MODULE_ID=tplinkStaticARPMIB, tpStaticARPConfigTable=tpStaticARPConfigTable, tplinkStaticARPMIB=tplinkStaticARPMIB, tpStaticARPItemMac=tpStaticARPItemMac)
