#
# PySNMP MIB module LEA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Integer32, Unsigned32, ModuleIdentity, TimeTicks, Bits, iso, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Integer32", "Unsigned32", "ModuleIdentity", "TimeTicks", "Bits", "iso", "Counter32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lea = ModuleIdentity((1, 3, 6, 1, 4, 1, 14841))
lea.setRevisions(('2002-09-26 00:00',))
if mibBuilder.loadTexts: lea.setLastUpdated('2002100400Z')
if mibBuilder.loadTexts: lea.setOrganization('www.leacom.fr')
leaSplitters = MibIdentifier((1, 3, 6, 1, 4, 1, 14841, 1))
leaExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 14841, 9999))
mibBuilder.exportSymbols("LEA-MIB", PYSNMP_MODULE_ID=lea, lea=lea, leaExperimental=leaExperimental, leaSplitters=leaSplitters)
