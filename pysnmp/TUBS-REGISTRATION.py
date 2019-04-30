#
# PySNMP MIB module TUBS-REGISTRATION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-REGISTRATION
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, enterprises, Counter64, ModuleIdentity, NotificationType, Gauge32, Unsigned32, IpAddress, iso, Bits, ObjectIdentity, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "enterprises", "Counter64", "ModuleIdentity", "NotificationType", "Gauge32", "Unsigned32", "IpAddress", "iso", "Bits", "ObjectIdentity", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tubs = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575))
tubs.setRevisions(('1997-02-14 10:23',))
if mibBuilder.loadTexts: tubs.setLastUpdated('9702141023Z')
if mibBuilder.loadTexts: tubs.setOrganization('TU Braunschweig')
ibr = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1))
mibBuilder.exportSymbols("TUBS-REGISTRATION", ibr=ibr, tubs=tubs, PYSNMP_MODULE_ID=tubs)
