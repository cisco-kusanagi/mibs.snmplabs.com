#
# PySNMP MIB module TPLINK-STATICARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-STATICARP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, ObjectIdentity, Gauge32, Counter32, MibIdentifier, iso, TimeTicks, Counter64, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter32", "MibIdentifier", "iso", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkStaticARPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 54))
tplinkStaticARPMIB.setRevisions(('2014-11-24 14:42',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkStaticARPMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkStaticARPMIB.setLastUpdated('201411241442Z')
if mibBuilder.loadTexts: tplinkStaticARPMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkStaticARPMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkStaticARPMIB.setDescription('Private MIB for static ARP configuration.')
tplinkStaticARPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1))
tplinkStaticARPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 2))
tpStaticARPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1))
tpStaticARPConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1), )
if mibBuilder.loadTexts: tpStaticARPConfigTable.setStatus('current')
if mibBuilder.loadTexts: tpStaticARPConfigTable.setDescription("A list of static ARP entries.ARP Presented here is a protocol that allows dynamic distribution of the information needed to build tables to translate an address A in protocol P's address space into a 48.bit Ethernet address.")
tpStaticARPConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-STATICARP-MIB", "tpStaticARPItemIp"))
if mibBuilder.loadTexts: tpStaticARPConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tpStaticARPConfigEntry.setDescription('The item can be added or removed .')
tpStaticARPItemIp = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticARPItemIp.setStatus('current')
if mibBuilder.loadTexts: tpStaticARPItemIp.setDescription('The ip Address of the ARP entry.')
tpStaticARPItemMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticARPItemMac.setStatus('current')
if mibBuilder.loadTexts: tpStaticARPItemMac.setDescription('The Mac (hardware) address of the ARP entry.')
tpStaticArpItemInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpStaticArpItemInterfaceName.setStatus('current')
if mibBuilder.loadTexts: tpStaticArpItemInterfaceName.setDescription('The name of the interface.')
tpStaticARPItemStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 54, 1, 1, 1, 1, 4), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpStaticARPItemStatus.setStatus('current')
if mibBuilder.loadTexts: tpStaticARPItemStatus.setDescription(' The following values are states: these values may be used as follow: active(1),if the entry is being used. notInService(2),destory the entry. notReady(3),destory the entry. createAndGo(4),not being used createAndWait(5),creat a new entry destroy(6),destory the entry.')
mibBuilder.exportSymbols("TPLINK-STATICARP-MIB", tplinkStaticARPMIBObjects=tplinkStaticARPMIBObjects, tpStaticARPConfigTable=tpStaticARPConfigTable, tpStaticARPConfig=tpStaticARPConfig, tpStaticARPItemStatus=tpStaticARPItemStatus, tplinkStaticARPMIB=tplinkStaticARPMIB, tpStaticARPItemMac=tpStaticARPItemMac, PYSNMP_MODULE_ID=tplinkStaticARPMIB, tpStaticArpItemInterfaceName=tpStaticArpItemInterfaceName, tpStaticARPConfigEntry=tpStaticARPConfigEntry, MacAddress=MacAddress, tplinkStaticARPNotifications=tplinkStaticARPNotifications, tpStaticARPItemIp=tpStaticARPItemIp)
