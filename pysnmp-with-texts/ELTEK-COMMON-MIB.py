#
# PySNMP MIB module ELTEK-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEK-COMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:00:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, iso, Counter64, NotificationType, Gauge32, Unsigned32, MibIdentifier, enterprises, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "iso", "Counter64", "NotificationType", "Gauge32", "Unsigned32", "MibIdentifier", "enterprises", "Counter32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltek = ModuleIdentity((1, 3, 6, 1, 4, 1, 12148))
eltek.setRevisions(('2011-11-25 09:58', '2011-10-17 13:34', '2011-08-19 09:16', '2011-08-19 09:47', '2011-09-05 11:28',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltek.setRevisionsDescriptions(('additional values to all alarm status enums', 'Major changes in OID order and names; added mains monitor energy log and generator fail status', 'hopefully final version. Stared implementation of eltek api', 'adjustment', 'fixed up mains group',))
if mibBuilder.loadTexts: eltek.setLastUpdated('201110171334Z')
if mibBuilder.loadTexts: eltek.setOrganization('ELTEK power System MIB Working Group')
if mibBuilder.loadTexts: eltek.setContactInfo('Eltek R&D. Postal: Eltek ASA P.O. Box 3043 N-3003 Drammen Norway Tel: +47-32 20 32 00 Fax: +47-32 20 31 20 web: www.eltek.com ')
if mibBuilder.loadTexts: eltek.setDescription('An ongoing effort toward a generic MIB for all ELTEK products. Branch overview: Aeongold branch will be 1 AL175 branch will be 2 AL6000 branch will be 3 Internal used branch will be 4 Internal used branch will be 5 OEM Smartpack branch will be 6 ELTEK Common branch will be 7 (SmartPack, MCU, AEON w/WebPower sw V2.x) ELTEK Distributed branch will be 8 (SmartPack w/WebPower sw V3.x) ELTEK Distributed V2 branch will be 9 (SmartPack w/WebPower sw V4.0) ELTEK Distributed V3 branch will be 9 (SmartPack w/WebPower sw V4.1) ELTEK Distributed V4 branch will be 9 (SmartPack w/WebPower sw V4.1, V4.2, V4.3, V4.5 and compack V1.0, V1.01, V1.02, V1.03) ELTEK Distributed V5 branch will be 9 (SmartPack w/WebPower sw V4.1, V4.2, V4.3, V4.5, V4.6) ELTEK Distributed V6 branch will be 9 (SmartPack2 sw V1.1, V1.2, V1.3) ELTEK Distributed V7 branch will be 9 (SmartPack w/WebPower sw V4.1, V4.2, V4.3, V4.5, V4.6, V4.7 and compack V1.xx) ELTEK eNexus MIB branch will be 10 (SmartPack2 and Compack) ELTEK Brasil office will have branch 11 ')
mibBuilder.exportSymbols("ELTEK-COMMON-MIB", eltek=eltek, PYSNMP_MODULE_ID=eltek)
