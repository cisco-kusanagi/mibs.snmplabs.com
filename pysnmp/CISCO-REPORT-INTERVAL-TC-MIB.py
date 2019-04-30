#
# PySNMP MIB module CISCO-REPORT-INTERVAL-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-REPORT-INTERVAL-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Gauge32, Counter64, ModuleIdentity, TimeTicks, IpAddress, MibIdentifier, Counter32, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Gauge32", "Counter64", "ModuleIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "Counter32", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoReportIntervalTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 670))
ciscoReportIntervalTcMIB.setRevisions(('2008-08-22 00:00',))
if mibBuilder.loadTexts: ciscoReportIntervalTcMIB.setLastUpdated('200808220000Z')
if mibBuilder.loadTexts: ciscoReportIntervalTcMIB.setOrganization('Cisco Systems, Inc.')
class ReportCurrentCount(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

class ReportIntervalCount(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

mibBuilder.exportSymbols("CISCO-REPORT-INTERVAL-TC-MIB", ReportCurrentCount=ReportCurrentCount, ReportIntervalCount=ReportIntervalCount, ciscoReportIntervalTcMIB=ciscoReportIntervalTcMIB, PYSNMP_MODULE_ID=ciscoReportIntervalTcMIB)
