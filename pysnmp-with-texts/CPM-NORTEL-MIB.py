#
# PySNMP MIB module CPM-NORTEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPM-NORTEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:27:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Bits, IpAddress, enterprises, Counter64, NotificationType, ModuleIdentity, TimeTicks, Unsigned32, ObjectIdentity, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Bits", "IpAddress", "enterprises", "Counter64", "NotificationType", "ModuleIdentity", "TimeTicks", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortel = ModuleIdentity((1, 3, 6, 1, 4, 1, 562))
if mibBuilder.loadTexts: nortel.setLastUpdated('9906231337Z')
if mibBuilder.loadTexts: nortel.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: nortel.setContactInfo('Nortel Customer Support Nortel Networks E-Mail: joedev@nortel.ca')
if mibBuilder.loadTexts: nortel.setDescription('')
dialaccess = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 14))
mibBuilder.exportSymbols("CPM-NORTEL-MIB", dialaccess=dialaccess, nortel=nortel, PYSNMP_MODULE_ID=nortel)
