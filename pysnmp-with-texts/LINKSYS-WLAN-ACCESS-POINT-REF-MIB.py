#
# PySNMP MIB module LINKSYS-WLAN-ACCESS-POINT-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LINKSYS-WLAN-ACCESS-POINT-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:07:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, Counter32, MibIdentifier, enterprises, Gauge32, Integer32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "Counter32", "MibIdentifier", "enterprises", "Gauge32", "Integer32", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
linksys = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955))
linksys.setRevisions(('2014-04-09 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: linksys.setRevisionsDescriptions(('Initial release.',))
if mibBuilder.loadTexts: linksys.setLastUpdated('201404090000Z')
if mibBuilder.loadTexts: linksys.setOrganization('Linksys, LLC. Corporation')
if mibBuilder.loadTexts: linksys.setContactInfo(' Postal: Linksys International, Inc. 131 Theory Drive Irvine, CA 92617 Tel: +1 949 270 8500')
if mibBuilder.loadTexts: linksys.setDescription('Wireless-AC Dual Band LAPAC1750PRO Access Point with PoE.')
smb = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000))
mibBuilder.exportSymbols("LINKSYS-WLAN-ACCESS-POINT-REF-MIB", PYSNMP_MODULE_ID=linksys, linksys=linksys, smb=smb)
