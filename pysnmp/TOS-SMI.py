#
# PySNMP MIB module TOS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TOS-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, TimeTicks, Counter64, MibIdentifier, Integer32, Gauge32, Bits, enterprises, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, NotificationType, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Counter64", "MibIdentifier", "Integer32", "Gauge32", "Bits", "enterprises", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "NotificationType", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
topsec = ModuleIdentity((1, 3, 6, 1, 4, 1, 14331))
topsec.setRevisions(('1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00', '1970-01-01 00:00',))
if mibBuilder.loadTexts: topsec.setLastUpdated('08-03-14')
if mibBuilder.loadTexts: topsec.setOrganization('TOPSEC')
topsecMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 14331, 5))
topsecExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 14331, 5, 4))
objects = MibIdentifier((1, 3, 6, 1, 4, 1, 14331, 5, 5))
tosMib = MibIdentifier((1, 3, 6, 1, 4, 1, 14331, 5, 5, 1))
mibBuilder.exportSymbols("TOS-SMI", PYSNMP_MODULE_ID=topsec, topsecExperiment=topsecExperiment, tosMib=tosMib, objects=objects, topsec=topsec, topsecMgmt=topsecMgmt)
