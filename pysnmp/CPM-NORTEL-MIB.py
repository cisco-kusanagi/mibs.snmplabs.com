#
# PySNMP MIB module CPM-NORTEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPM-NORTEL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Bits, NotificationType, enterprises, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Bits", "NotificationType", "enterprises", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortel = ModuleIdentity((1, 3, 6, 1, 4, 1, 562))
if mibBuilder.loadTexts: nortel.setLastUpdated('9906231337Z')
if mibBuilder.loadTexts: nortel.setOrganization('Nortel Networks')
dialaccess = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 14))
mibBuilder.exportSymbols("CPM-NORTEL-MIB", dialaccess=dialaccess, nortel=nortel, PYSNMP_MODULE_ID=nortel)
