#
# PySNMP MIB module WS-INFRA-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WS-INFRA-NTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:30:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, TimeTicks, Integer32, Bits, Counter32, Counter64, ModuleIdentity, Unsigned32, ObjectIdentity, iso, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "TimeTicks", "Integer32", "Bits", "Counter32", "Counter64", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "iso", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DateAndTime, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "TruthValue", "DisplayString")
wsInfraNTP, = mibBuilder.importSymbols("WS-INFRA-SMI-MIB", "wsInfraNTP")
wsInfraNTPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1))
wsInfraNTPMIB.setRevisions(('2006-05-26 12:37', '2005-10-12 14:21', '2005-08-12 13:58', '2005-06-28 11:58', '2005-06-27 14:34', '2005-06-24 12:07', '2005-06-23 13:17', '2005-06-22 10:34', '2005-06-20 11:05', '2005-06-09 15:24', '2005-06-07 18:43', '2005-05-04 16:13', '2005-05-04 10:58',))
if mibBuilder.loadTexts: wsInfraNTPMIB.setLastUpdated('200506271058Z')
if mibBuilder.loadTexts: wsInfraNTPMIB.setOrganization('Symbol Technologies')
wsInfraNtpEnable = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraNtpEnable.setStatus('obsolete')
wsInfraNtp1Server = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraNtp1Server.setStatus('obsolete')
wsInfraNtp2Server = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraNtp2Server.setStatus('obsolete')
wsInfraNtp3Server = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraNtp3Server.setStatus('obsolete')
wsInfraNtpTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraNtpTimeZone.setStatus('current')
wsInfraNtpCurrentDateTime = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 6), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wsInfraNtpCurrentDateTime.setStatus('current')
wsInfraNtpAllTimeZones = MibScalar((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 5000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wsInfraNtpAllTimeZones.setStatus('current')
wsInfraNTPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100))
wsInfraNTPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 1))
wsInfraNTPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 1, 1)).setObjects(("WS-INFRA-NTP-MIB", "wsInfraNtpAllTimeZones"), ("WS-INFRA-NTP-MIB", "wsInfraNtpCurrentDateTime"), ("WS-INFRA-NTP-MIB", "wsInfraNtpTimeZone"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wsInfraNTPGroup = wsInfraNTPGroup.setStatus('current')
wsInfraNTPGroupObsolete = ObjectGroup((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 1, 2)).setObjects(("WS-INFRA-NTP-MIB", "wsInfraNtpEnable"), ("WS-INFRA-NTP-MIB", "wsInfraNtp1Server"), ("WS-INFRA-NTP-MIB", "wsInfraNtp2Server"), ("WS-INFRA-NTP-MIB", "wsInfraNtp3Server"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wsInfraNTPGroupObsolete = wsInfraNTPGroupObsolete.setStatus('obsolete')
wsInfraNTPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 2))
wsInfraNTPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 388, 14, 1, 10, 1, 100, 2, 1)).setObjects(("WS-INFRA-NTP-MIB", "wsInfraNTPGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wsInfraNTPMIBCompliance = wsInfraNTPMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("WS-INFRA-NTP-MIB", wsInfraNTPMIBCompliance=wsInfraNTPMIBCompliance, wsInfraNtpEnable=wsInfraNtpEnable, wsInfraNtpTimeZone=wsInfraNtpTimeZone, wsInfraNtpCurrentDateTime=wsInfraNtpCurrentDateTime, wsInfraNtp2Server=wsInfraNtp2Server, wsInfraNTPMIBConformance=wsInfraNTPMIBConformance, wsInfraNTPMIBGroups=wsInfraNTPMIBGroups, wsInfraNTPGroup=wsInfraNTPGroup, wsInfraNTPMIB=wsInfraNTPMIB, wsInfraNTPGroupObsolete=wsInfraNTPGroupObsolete, PYSNMP_MODULE_ID=wsInfraNTPMIB, wsInfraNtpAllTimeZones=wsInfraNtpAllTimeZones, wsInfraNtp3Server=wsInfraNtp3Server, wsInfraNTPMIBCompliances=wsInfraNTPMIBCompliances, wsInfraNtp1Server=wsInfraNtp1Server)
