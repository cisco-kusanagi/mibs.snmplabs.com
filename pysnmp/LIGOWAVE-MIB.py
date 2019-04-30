#
# PySNMP MIB module LIGOWAVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIGOWAVE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:56:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Counter32, iso, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, enterprises, ModuleIdentity, Unsigned32, Gauge32, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter32", "iso", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "enterprises", "ModuleIdentity", "Unsigned32", "Gauge32", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ligowave = ModuleIdentity((1, 3, 6, 1, 4, 1, 32750))
ligowave.setRevisions(('2008-09-05 00:00',))
if mibBuilder.loadTexts: ligowave.setLastUpdated('200809050000Z')
if mibBuilder.loadTexts: ligowave.setOrganization('LigoWave')
ligoProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 1))
ligoAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 2))
ligoMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3))
ligoExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 7))
mibBuilder.exportSymbols("LIGOWAVE-MIB", ligoMgmt=ligoMgmt, PYSNMP_MODULE_ID=ligowave, ligoExperimental=ligoExperimental, ligoProducts=ligoProducts, ligoAdmin=ligoAdmin, ligowave=ligowave)
