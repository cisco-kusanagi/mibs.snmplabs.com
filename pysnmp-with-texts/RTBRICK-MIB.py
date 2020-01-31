#
# PySNMP MIB module RTBRICK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/RTBRICK-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:35:45 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, ModuleIdentity, IpAddress, NotificationType, Bits, Integer32, Counter64, ObjectIdentity, enterprises, TimeTicks, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "ModuleIdentity", "IpAddress", "NotificationType", "Bits", "Integer32", "Counter64", "ObjectIdentity", "enterprises", "TimeTicks", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TestAndIncr, RowStatus, AutonomousType, TimeStamp, TextualConvention, TruthValue, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TestAndIncr", "RowStatus", "AutonomousType", "TimeStamp", "TextualConvention", "TruthValue", "PhysAddress")
rtbrick = ModuleIdentity((1, 3, 6, 1, 4, 1, 50058))
rtbrick.setRevisions(('2019-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rtbrick.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: rtbrick.setLastUpdated('201804140000Z')
if mibBuilder.loadTexts: rtbrick.setOrganization('RtBrick')
if mibBuilder.loadTexts: rtbrick.setContactInfo('E-mail: Stefan Lieberth <stefan@rtbrick.com>')
if mibBuilder.loadTexts: rtbrick.setDescription('RtBrick top-level MIB tree infrastructure')
rtbrickTables = MibIdentifier((1, 3, 6, 1, 4, 1, 50058, 101))
rtbrickProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 50058, 102))
rtbrickTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 50058, 103))
rtbrickSyslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 50058, 103, 1))
rtbrickModules = MibIdentifier((1, 3, 6, 1, 4, 1, 50058, 104))
mibBuilder.exportSymbols("RTBRICK-MIB", rtbrickTraps=rtbrickTraps, PYSNMP_MODULE_ID=rtbrick, rtbrickTables=rtbrickTables, rtbrickModules=rtbrickModules, rtbrickProducts=rtbrickProducts, rtbrickSyslogNotifications=rtbrickSyslogNotifications, rtbrick=rtbrick)
