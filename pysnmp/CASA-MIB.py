#
# PySNMP MIB module CASA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CASA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Gauge32, Counter32, Integer32, Counter64, NotificationType, MibIdentifier, ObjectIdentity, enterprises, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Gauge32", "Counter32", "Integer32", "Counter64", "NotificationType", "MibIdentifier", "ObjectIdentity", "enterprises", "ModuleIdentity", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
casa = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858))
casa.setRevisions(('2006-03-22 00:00', '2006-03-22 00:00',))
if mibBuilder.loadTexts: casa.setLastUpdated('200407080000Z')
if mibBuilder.loadTexts: casa.setOrganization('Casa Systems Inc.')
mibBuilder.exportSymbols("CASA-MIB", casa=casa, PYSNMP_MODULE_ID=casa)
