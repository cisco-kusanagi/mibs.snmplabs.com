#
# PySNMP MIB module GNOME-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GNOME-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, MibIdentifier, Bits, Counter32, Integer32, iso, TimeTicks, Counter64, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "MibIdentifier", "Bits", "Counter32", "Integer32", "iso", "TimeTicks", "Counter64", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gnome = ModuleIdentity((1, 3, 6, 1, 4, 1, 3319))
gnome.setRevisions(('2007-09-07 00:00', '2005-05-07 00:00', '2003-12-07 00:00', '1998-09-01 00:00',))
if mibBuilder.loadTexts: gnome.setLastUpdated('200709070000Z')
if mibBuilder.loadTexts: gnome.setOrganization('GNOME project')
gnomeProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 1))
if mibBuilder.loadTexts: gnomeProducts.setStatus('current')
gnomeMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 2))
if mibBuilder.loadTexts: gnomeMgmt.setStatus('current')
gnomeTest = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 3))
if mibBuilder.loadTexts: gnomeTest.setStatus('current')
gnomeSysadmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 4))
if mibBuilder.loadTexts: gnomeSysadmin.setStatus('current')
gnomeLDAP = ObjectIdentity((1, 3, 6, 1, 4, 1, 3319, 5))
if mibBuilder.loadTexts: gnomeLDAP.setStatus('current')
mibBuilder.exportSymbols("GNOME-SMI", gnomeTest=gnomeTest, gnome=gnome, gnomeMgmt=gnomeMgmt, gnomeProducts=gnomeProducts, PYSNMP_MODULE_ID=gnome, gnomeLDAP=gnomeLDAP, gnomeSysadmin=gnomeSysadmin)
