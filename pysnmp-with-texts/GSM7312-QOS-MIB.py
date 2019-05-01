#
# PySNMP MIB module GSM7312-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7312-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:20:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
gsm7312, = mibBuilder.importSymbols("GSM7312-REF-MIB", "gsm7312")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, Counter32, ModuleIdentity, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, IpAddress, MibIdentifier, Integer32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Counter32", "ModuleIdentity", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "IpAddress", "MibIdentifier", "Integer32", "iso", "Counter64")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
gsm7312QOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 6, 3))
gsm7312QOS.setRevisions(('2003-05-06 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gsm7312QOS.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: gsm7312QOS.setLastUpdated('200305061200Z')
if mibBuilder.loadTexts: gsm7312QOS.setOrganization('Netgear')
if mibBuilder.loadTexts: gsm7312QOS.setContactInfo('')
if mibBuilder.loadTexts: gsm7312QOS.setDescription('')
mibBuilder.exportSymbols("GSM7312-QOS-MIB", PYSNMP_MODULE_ID=gsm7312QOS, gsm7312QOS=gsm7312QOS)
