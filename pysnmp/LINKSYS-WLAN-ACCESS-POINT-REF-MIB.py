#
# PySNMP MIB module LINKSYS-WLAN-ACCESS-POINT-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LINKSYS-WLAN-ACCESS-POINT-REF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter64, IpAddress, Integer32, Gauge32, MibIdentifier, TimeTicks, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Counter32, ObjectIdentity, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "IpAddress", "Integer32", "Gauge32", "MibIdentifier", "TimeTicks", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Counter32", "ObjectIdentity", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
linksys = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955))
linksys.setRevisions(('2014-04-09 12:00',))
if mibBuilder.loadTexts: linksys.setLastUpdated('201404090000Z')
if mibBuilder.loadTexts: linksys.setOrganization('Linksys, LLC. Corporation')
smb = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000))
mibBuilder.exportSymbols("LINKSYS-WLAN-ACCESS-POINT-REF-MIB", smb=smb, PYSNMP_MODULE_ID=linksys, linksys=linksys)
