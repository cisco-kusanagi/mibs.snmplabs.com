#
# PySNMP MIB module GSM7324-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GSM7324-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:20:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
gsm7324, = mibBuilder.importSymbols("GSM7324-REF-MIB", "gsm7324")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, Unsigned32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, MibIdentifier, Gauge32, TimeTicks, ObjectIdentity, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Unsigned32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "MibIdentifier", "Gauge32", "TimeTicks", "ObjectIdentity", "Counter64", "iso")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
gsm7324QOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 7, 3))
gsm7324QOS.setRevisions(('2003-05-06 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gsm7324QOS.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: gsm7324QOS.setLastUpdated('200305061200Z')
if mibBuilder.loadTexts: gsm7324QOS.setOrganization('Netgear')
if mibBuilder.loadTexts: gsm7324QOS.setContactInfo('')
if mibBuilder.loadTexts: gsm7324QOS.setDescription('')
mibBuilder.exportSymbols("GSM7324-QOS-MIB", PYSNMP_MODULE_ID=gsm7324QOS, gsm7324QOS=gsm7324QOS)
