#
# PySNMP MIB module GSM7324-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7324-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
gsm7324, = mibBuilder.importSymbols("GSM7324-REF-MIB", "gsm7324")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, TimeTicks, Gauge32, NotificationType, ModuleIdentity, IpAddress, Integer32, iso, Unsigned32, Bits, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "TimeTicks", "Gauge32", "NotificationType", "ModuleIdentity", "IpAddress", "Integer32", "iso", "Unsigned32", "Bits", "Counter32", "MibIdentifier")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
gsm7324QOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 7, 3))
gsm7324QOS.setRevisions(('2003-05-06 12:00',))
if mibBuilder.loadTexts: gsm7324QOS.setLastUpdated('200305061200Z')
if mibBuilder.loadTexts: gsm7324QOS.setOrganization('Netgear')
mibBuilder.exportSymbols("GSM7324-QOS-MIB", gsm7324QOS=gsm7324QOS, PYSNMP_MODULE_ID=gsm7324QOS)
