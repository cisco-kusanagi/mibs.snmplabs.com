#
# PySNMP MIB module GSM7312-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7312-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
gsm7312, = mibBuilder.importSymbols("GSM7312-REF-MIB", "gsm7312")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, Bits, Integer32, Counter64, MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Bits", "Integer32", "Counter64", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "IpAddress", "TimeTicks")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
gsm7312QOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 6, 3))
gsm7312QOS.setRevisions(('2003-05-06 12:00',))
if mibBuilder.loadTexts: gsm7312QOS.setLastUpdated('200305061200Z')
if mibBuilder.loadTexts: gsm7312QOS.setOrganization('Netgear')
mibBuilder.exportSymbols("GSM7312-QOS-MIB", PYSNMP_MODULE_ID=gsm7312QOS, gsm7312QOS=gsm7312QOS)
