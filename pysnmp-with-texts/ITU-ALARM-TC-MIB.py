#
# PySNMP MIB module ITU-ALARM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ITU-ALARM-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Unsigned32, Counter32, mib_2, IpAddress, TimeTicks, Counter64, ObjectIdentity, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Unsigned32", "Counter32", "mib-2", "IpAddress", "TimeTicks", "Counter64", "ObjectIdentity", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ituAlarmTc = ModuleIdentity((1, 3, 6, 1, 2, 1, 120))
ituAlarmTc.setRevisions(('2004-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ituAlarmTc.setRevisionsDescriptions(('Initial version, published as RFC 3877.',))
if mibBuilder.loadTexts: ituAlarmTc.setLastUpdated('200409090000Z')
if mibBuilder.loadTexts: ituAlarmTc.setOrganization('IETF Distributed Management Working Group')
if mibBuilder.loadTexts: ituAlarmTc.setContactInfo(' WG EMail: disman@ietf.org Subscribe: disman-request@ietf.org http://www.ietf.org/html.charters/disman-charter.html Chair: Randy Presuhn randy_presuhn@mindspring.com Editors: Sharon Chisholm Nortel Networks PO Box 3511 Station C Ottawa, Ont. K1Y 4H7 Canada schishol@nortelnetworks.com Dan Romascanu Avaya Atidim Technology Park, Bldg. #3 Tel Aviv, 61131 Israel Tel: +972-3-645-8414 Email: dromasca@avaya.com')
if mibBuilder.loadTexts: ituAlarmTc.setDescription('This MIB module defines the ITU Alarm textual convention for objects not expected to require regular extension. Copyright (C) The Internet Society (2004). The initial version of this MIB module was published in RFC 3877. For full legal notices see the RFC itself. Supplementary information may be available on: http://www.ietf.org/copyrights/ianamib.html')
class ItuPerceivedSeverity(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information Model', 1995 ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992"
    description = 'ITU perceived severity values'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("indeterminate", 2), ("critical", 3), ("major", 4), ("minor", 5), ("warning", 6))

class ItuTrendIndication(TextualConvention, Integer32):
    reference = "ITU Recommendation M.3100, 'Generic Network Information Model', 1995 ITU Recommendation X.733, 'Information Technology - Open Systems Interconnection - System Management: Alarm Reporting Function', 1992"
    description = 'ITU trend indication values for alarms.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("moreSevere", 1), ("noChange", 2), ("lessSevere", 3))

mibBuilder.exportSymbols("ITU-ALARM-TC-MIB", ItuPerceivedSeverity=ItuPerceivedSeverity, ItuTrendIndication=ItuTrendIndication, PYSNMP_MODULE_ID=ituAlarmTc, ituAlarmTc=ituAlarmTc)
