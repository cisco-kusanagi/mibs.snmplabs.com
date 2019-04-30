#
# PySNMP MIB module HP-ICF-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-NTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:22:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Gauge32, Bits, Integer32, IpAddress, iso, NotificationType, Unsigned32, ModuleIdentity, Counter64, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Bits", "Integer32", "IpAddress", "iso", "NotificationType", "Unsigned32", "ModuleIdentity", "Counter64", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
hpicfNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121))
hpicfNtpMIB.setRevisions(('2017-08-22 00:00', '2016-02-10 00:00', '2015-07-01 00:00',))
if mibBuilder.loadTexts: hpicfNtpMIB.setLastUpdated('201708220000Z')
if mibBuilder.loadTexts: hpicfNtpMIB.setOrganization('HP Networking')
hpicfNtpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1))
hpicfNtpConfigScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1))
hpicfNtpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 2))
hpicfNtpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpAdminStatus.setStatus('current')
hpicfNtpConfigMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("unicast", 2), ("broadcast", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpConfigMode.setStatus('current')
hpicfNtpMaxAssociation = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpMaxAssociation.setStatus('current')
hpicfNtpStatusReferenceTimeFrac = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpStatusReferenceTimeFrac.setStatus('current')
hpicfNtpStatusReferenceTimeSec = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpStatusReferenceTimeSec.setStatus('current')
hpicfNtpStatusClockOffset = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpStatusClockOffset.setStatus('current')
hpicfNtpStatusRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpStatusRootDelay.setStatus('current')
hpicfNtpStatusRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpStatusRootDispersion.setStatus('current')
hpicfNtpAssoDrift = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoDrift.setStatus('current')
hpicfNtpInetConfigServerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2), )
if mibBuilder.loadTexts: hpicfNtpInetConfigServerTable.setStatus('current')
hpicfNtpInetConfigServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1), ).setIndexNames((0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddressType"), (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddress"))
if mibBuilder.loadTexts: hpicfNtpInetConfigServerEntry.setStatus('current')
hpicfNtpInetServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: hpicfNtpInetServerAddressType.setStatus('current')
hpicfNtpInetServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: hpicfNtpInetServerAddress.setStatus('current')
hpicfNtpInetServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpInetServerRowStatus.setStatus('current')
hpicfNtpInetServerAuthKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpInetServerAuthKeyId.setStatus('current')
hpicfNtpConfigPollMinInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 17)).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpConfigPollMinInterval.setStatus('current')
hpicfNtpConfigPollMaxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 17)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpConfigPollMaxInterval.setStatus('current')
hpicfNtpAssoBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noburst", 1), ("burst", 2), ("iburst", 3))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpAssoBurst.setStatus('current')
hpicfNtpAssoIsOobm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 2, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpAssoIsOobm.setStatus('current')
hpicfNtpInetServerInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3), )
if mibBuilder.loadTexts: hpicfNtpInetServerInfoTable.setStatus('current')
hpicfNtpInetServerInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1), ).setIndexNames((0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddressType"), (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddress"))
if mibBuilder.loadTexts: hpicfNtpInetServerInfoEntry.setStatus('current')
hpicfNtpAssoOurPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoOurPollInterval.setStatus('current')
hpicfNtpAssoPeerPollInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoPeerPollInterval.setStatus('current')
hpicfNtpAssoRootDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoRootDelay.setStatus('current')
hpicfNtpAssoRootDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoRootDispersion.setStatus('current')
hpicfNtpAssoPeerReach = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoPeerReach.setStatus('current')
hpicfNtpAssoOriginTimeFrac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoOriginTimeFrac.setStatus('current')
hpicfNtpAssoOriginTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoOriginTimeSec.setStatus('current')
hpicfNtpAssoRecvTimeFrac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoRecvTimeFrac.setStatus('current')
hpicfNtpAssoRecvTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoRecvTimeSec.setStatus('current')
hpicfNtpAssoXmtTimeFrac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoXmtTimeFrac.setStatus('current')
hpicfNtpAssoXmtTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoXmtTimeSec.setStatus('current')
hpicfNtpAssolastPollreq = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssolastPollreq.setStatus('current')
hpicfNtpAssoPrecision = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoPrecision.setStatus('current')
hpicfNtpAssoCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 99))).clone(namedValues=NamedValues(("synchronized", 1), ("notsynchronized", 2), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoCurrentMode.setStatus('current')
hpicfNtpAssoPeerDispersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 3, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpAssoPeerDispersion.setStatus('current')
hpicfNtpAuthenticationKeyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4), )
if mibBuilder.loadTexts: hpicfNtpAuthenticationKeyTable.setStatus('current')
hpicfNtpAuthenticationKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1), ).setIndexNames((0, "HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyId"))
if mibBuilder.loadTexts: hpicfNtpAuthenticationKeyEntry.setStatus('current')
hpicfNtpAuthenticationKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: hpicfNtpAuthenticationKeyId.setStatus('current')
hpicfNtpAuthenticationKeyAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("md5", 2), ("sha1", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpAuthenticationKeyAuthMode.setStatus('current')
hpicfNtpAuthenticationKeyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpAuthenticationKeyValue.setStatus('current')
hpicfNtpAuthenticationKeyTrusted = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 4), TruthValue().clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpAuthenticationKeyTrusted.setStatus('current')
hpicfNtpAuthenticationKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpAuthenticationKeyRowStatus.setStatus('current')
hpicfNtpAuthenticationKeyEncrypted = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpAuthenticationKeyEncrypted.setStatus('current')
hpicfNtpIpv6MulticastTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 5), )
if mibBuilder.loadTexts: hpicfNtpIpv6MulticastTable.setStatus('current')
hpicfNtpIpv6MulticastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfNtpIpv6MulticastEntry.setStatus('current')
hpicfNtpIpv6Multicast = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 5, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpIpv6Multicast.setStatus('current')
hpicfNtpIpv6MulticastStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpIpv6MulticastStatus.setStatus('current')
hpicfNtpAssoSampleTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7), )
if mibBuilder.loadTexts: hpicfNtpAssoSampleTable.setStatus('current')
hpicfNtpAssoSampleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7, 1), ).setIndexNames((0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddressType"), (0, "HP-ICF-NTP-MIB", "hpicfNtpInetServerAddress"), (0, "HP-ICF-NTP-MIB", "hpicfNtpAssoSampleId"))
if mibBuilder.loadTexts: hpicfNtpAssoSampleEntry.setStatus('current')
hpicfNtpAssoSampleId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpicfNtpAssoSampleId.setStatus('current')
hpicfNtpfiltDelaySample = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpfiltDelaySample.setStatus('current')
hpicfNtpfiltOffsetSample = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpfiltOffsetSample.setStatus('current')
hpicfNtpInetServerNameTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8), )
if mibBuilder.loadTexts: hpicfNtpInetServerNameTable.setStatus('current')
hpicfNtpInetServerNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1), ).setIndexNames((0, "HP-ICF-NTP-MIB", "hpicfNtpServerNameIndex"))
if mibBuilder.loadTexts: hpicfNtpInetServerNameEntry.setStatus('current')
hpicfNtpServerNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: hpicfNtpServerNameIndex.setStatus('current')
hpicfNtpInetServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpInetServerName.setStatus('current')
hpicfNtpInetServerNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfNtpInetServerNameRowStatus.setStatus('current')
hpicfNtpServerNameResolvAddType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpServerNameResolvAddType.setStatus('current')
hpicfNtpServerNameResolvAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 5), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpServerNameResolvAddress.setStatus('current')
hpicfNtpServerNameResolveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notattempted", 0), ("active", 1), ("dnsunknownhost", 2), ("dnsnotresponding", 3), ("dnsfailed", 4), ("notactive", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfNtpServerNameResolveStatus.setStatus('current')
hpicfNtpInetServerNameAuthKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpInetServerNameAuthKeyId.setStatus('current')
hpicfNtpConfigServerNamePollMinInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 17)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpConfigServerNamePollMinInterval.setStatus('current')
hpicfNtpConfigServerNamePollMaxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 17)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpConfigServerNamePollMaxInterval.setStatus('current')
hpicfNtpServerNameAssoBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noburst", 1), ("burst", 2), ("iburst", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpServerNameAssoBurst.setStatus('current')
hpicfNtpServerNameAssoIsOobm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 1, 8, 1, 11), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfNtpServerNameAssoIsOobm.setStatus('current')
hpicfNtpConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3))
hpicfNtpConfigCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1))
hpicfNtpConfigGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2))
hpicfNtpInetConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 1)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpConfigGroup"), ("HP-ICF-NTP-MIB", "hpicfNtpInetServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpInetConfigCompliance = hpicfNtpInetConfigCompliance.setStatus('current')
hpicfNtpAuthenticationConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 2)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyIdConfigGroup"), ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyIdConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpAuthenticationConfigCompliance = hpicfNtpAuthenticationConfigCompliance.setStatus('current')
hpicfNtpServerConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 3)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpInetServerConfigGroup"), ("HP-ICF-NTP-MIB", "hpicfNtpInetServerConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpServerConfigCompliance = hpicfNtpServerConfigCompliance.setStatus('current')
hpicfNtpAssoSampleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 4)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpAssociationSampleGroup"), ("HP-ICF-NTP-MIB", "hpicfNtpAssociationSampleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpAssoSampleCompliance = hpicfNtpAssoSampleCompliance.setStatus('current')
hpicfNtpServerNameCfgCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 1, 5)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpInetServerNameCfgGroup"), ("HP-ICF-NTP-MIB", "hpicfNtpInetServerNameCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpServerNameCfgCompliance = hpicfNtpServerNameCfgCompliance.setStatus('current')
hpicfNtpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 1)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpConfigMode"), ("HP-ICF-NTP-MIB", "hpicfNtpMaxAssociation"), ("HP-ICF-NTP-MIB", "hpicfNtpAdminStatus"), ("HP-ICF-NTP-MIB", "hpicfNtpStatusReferenceTimeFrac"), ("HP-ICF-NTP-MIB", "hpicfNtpStatusReferenceTimeSec"), ("HP-ICF-NTP-MIB", "hpicfNtpStatusClockOffset"), ("HP-ICF-NTP-MIB", "hpicfNtpStatusRootDelay"), ("HP-ICF-NTP-MIB", "hpicfNtpStatusRootDispersion"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoDrift"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpConfigGroup = hpicfNtpConfigGroup.setStatus('current')
hpicfNtpInetServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 2)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpInetServerRowStatus"), ("HP-ICF-NTP-MIB", "hpicfNtpInetServerAuthKeyId"), ("HP-ICF-NTP-MIB", "hpicfNtpConfigPollMinInterval"), ("HP-ICF-NTP-MIB", "hpicfNtpConfigPollMaxInterval"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoOurPollInterval"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoPeerPollInterval"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoRootDelay"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoRootDispersion"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoPeerReach"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoOriginTimeFrac"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoOriginTimeSec"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoRecvTimeFrac"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoRecvTimeSec"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoXmtTimeFrac"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoXmtTimeSec"), ("HP-ICF-NTP-MIB", "hpicfNtpAssolastPollreq"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoPrecision"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoCurrentMode"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoPeerDispersion"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoBurst"), ("HP-ICF-NTP-MIB", "hpicfNtpAssoIsOobm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpInetServerConfigGroup = hpicfNtpInetServerConfigGroup.setStatus('current')
hpicfNtpAuthenticationKeyIdConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 3)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyAuthMode"), ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyValue"), ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyEncrypted"), ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyTrusted"), ("HP-ICF-NTP-MIB", "hpicfNtpAuthenticationKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpAuthenticationKeyIdConfigGroup = hpicfNtpAuthenticationKeyIdConfigGroup.setStatus('current')
hpicfNtpAssociationSampleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 4)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpfiltDelaySample"), ("HP-ICF-NTP-MIB", "hpicfNtpfiltOffsetSample"), ("HP-ICF-NTP-MIB", "hpicfNtpIpv6Multicast"), ("HP-ICF-NTP-MIB", "hpicfNtpIpv6MulticastStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpAssociationSampleGroup = hpicfNtpAssociationSampleGroup.setStatus('current')
hpicfNtpInetServerNameCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121, 3, 2, 5)).setObjects(("HP-ICF-NTP-MIB", "hpicfNtpInetServerName"), ("HP-ICF-NTP-MIB", "hpicfNtpInetServerNameRowStatus"), ("HP-ICF-NTP-MIB", "hpicfNtpServerNameResolvAddType"), ("HP-ICF-NTP-MIB", "hpicfNtpServerNameResolvAddress"), ("HP-ICF-NTP-MIB", "hpicfNtpServerNameResolveStatus"), ("HP-ICF-NTP-MIB", "hpicfNtpInetServerNameAuthKeyId"), ("HP-ICF-NTP-MIB", "hpicfNtpConfigServerNamePollMinInterval"), ("HP-ICF-NTP-MIB", "hpicfNtpConfigServerNamePollMaxInterval"), ("HP-ICF-NTP-MIB", "hpicfNtpServerNameAssoBurst"), ("HP-ICF-NTP-MIB", "hpicfNtpServerNameAssoIsOobm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfNtpInetServerNameCfgGroup = hpicfNtpInetServerNameCfgGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-NTP-MIB", hpicfNtpAssoSampleCompliance=hpicfNtpAssoSampleCompliance, hpicfNtpConfigServerNamePollMinInterval=hpicfNtpConfigServerNamePollMinInterval, hpicfNtpAuthenticationKeyEncrypted=hpicfNtpAuthenticationKeyEncrypted, hpicfNtpInetServerNameAuthKeyId=hpicfNtpInetServerNameAuthKeyId, hpicfNtpAuthenticationKeyRowStatus=hpicfNtpAuthenticationKeyRowStatus, hpicfNtpStatusReferenceTimeFrac=hpicfNtpStatusReferenceTimeFrac, hpicfNtpConfigServerNamePollMaxInterval=hpicfNtpConfigServerNamePollMaxInterval, hpicfNtpInetServerRowStatus=hpicfNtpInetServerRowStatus, hpicfNtpAssoBurst=hpicfNtpAssoBurst, hpicfNtpAssoPeerPollInterval=hpicfNtpAssoPeerPollInterval, hpicfNtpServerNameAssoBurst=hpicfNtpServerNameAssoBurst, hpicfNtpStatusReferenceTimeSec=hpicfNtpStatusReferenceTimeSec, hpicfNtpAuthenticationKeyId=hpicfNtpAuthenticationKeyId, hpicfNtpMaxAssociation=hpicfNtpMaxAssociation, PYSNMP_MODULE_ID=hpicfNtpMIB, hpicfNtpServerNameIndex=hpicfNtpServerNameIndex, hpicfNtpAssoRootDelay=hpicfNtpAssoRootDelay, hpicfNtpAssoPeerReach=hpicfNtpAssoPeerReach, hpicfNtpInetServerInfoTable=hpicfNtpInetServerInfoTable, hpicfNtpInetServerName=hpicfNtpInetServerName, hpicfNtpAssoIsOobm=hpicfNtpAssoIsOobm, hpicfNtpConfigCompliances=hpicfNtpConfigCompliances, hpicfNtpInetServerNameRowStatus=hpicfNtpInetServerNameRowStatus, hpicfNtpMIB=hpicfNtpMIB, hpicfNtpIpv6MulticastTable=hpicfNtpIpv6MulticastTable, hpicfNtpAuthenticationKeyEntry=hpicfNtpAuthenticationKeyEntry, hpicfNtpConfigScalars=hpicfNtpConfigScalars, hpicfNtpInetServerNameEntry=hpicfNtpInetServerNameEntry, hpicfNtpInetServerInfoEntry=hpicfNtpInetServerInfoEntry, hpicfNtpAuthenticationKeyValue=hpicfNtpAuthenticationKeyValue, hpicfNtpServerNameCfgCompliance=hpicfNtpServerNameCfgCompliance, hpicfNtpStatusRootDelay=hpicfNtpStatusRootDelay, hpicfNtpAssociationSampleGroup=hpicfNtpAssociationSampleGroup, hpicfNtpAssoCurrentMode=hpicfNtpAssoCurrentMode, hpicfNtpStatusClockOffset=hpicfNtpStatusClockOffset, hpicfNtpInetServerNameCfgGroup=hpicfNtpInetServerNameCfgGroup, hpicfNtpAssoOurPollInterval=hpicfNtpAssoOurPollInterval, hpicfNtpIpv6MulticastEntry=hpicfNtpIpv6MulticastEntry, hpicfNtpServerNameResolvAddress=hpicfNtpServerNameResolvAddress, hpicfNtpAssoOriginTimeSec=hpicfNtpAssoOriginTimeSec, hpicfNtpAuthenticationConfigCompliance=hpicfNtpAuthenticationConfigCompliance, hpicfNtpAssoPeerDispersion=hpicfNtpAssoPeerDispersion, hpicfNtpInetConfigServerTable=hpicfNtpInetConfigServerTable, hpicfNtpConfigGroup=hpicfNtpConfigGroup, hpicfNtpAuthenticationKeyIdConfigGroup=hpicfNtpAuthenticationKeyIdConfigGroup, hpicfNtpfiltDelaySample=hpicfNtpfiltDelaySample, hpicfNtpAssoDrift=hpicfNtpAssoDrift, hpicfNtpIpv6MulticastStatus=hpicfNtpIpv6MulticastStatus, hpicfNtpIpv6Multicast=hpicfNtpIpv6Multicast, hpicfNtpAdminStatus=hpicfNtpAdminStatus, hpicfNtpAssoPrecision=hpicfNtpAssoPrecision, hpicfNtpInetServerAddress=hpicfNtpInetServerAddress, hpicfNtpServerNameResolvAddType=hpicfNtpServerNameResolvAddType, hpicfNtpInetConfigCompliance=hpicfNtpInetConfigCompliance, hpicfNtpAssoRecvTimeFrac=hpicfNtpAssoRecvTimeFrac, hpicfNtpAuthenticationKeyTable=hpicfNtpAuthenticationKeyTable, hpicfNtpServerNameResolveStatus=hpicfNtpServerNameResolveStatus, hpicfNtpfiltOffsetSample=hpicfNtpfiltOffsetSample, hpicfNtpAssoSampleId=hpicfNtpAssoSampleId, hpicfNtpServerConfigCompliance=hpicfNtpServerConfigCompliance, hpicfNtpConfigMode=hpicfNtpConfigMode, hpicfNtpInetConfigServerEntry=hpicfNtpInetConfigServerEntry, hpicfNtpConfigGroups=hpicfNtpConfigGroups, hpicfNtpAssoXmtTimeSec=hpicfNtpAssoXmtTimeSec, hpicfNtpAssoRootDispersion=hpicfNtpAssoRootDispersion, hpicfNtpAuthenticationKeyAuthMode=hpicfNtpAuthenticationKeyAuthMode, hpicfNtpInetServerAddressType=hpicfNtpInetServerAddressType, hpicfNtpAssoOriginTimeFrac=hpicfNtpAssoOriginTimeFrac, hpicfNtpConfigConformance=hpicfNtpConfigConformance, hpicfNtpAssoSampleEntry=hpicfNtpAssoSampleEntry, hpicfNtpServerNameAssoIsOobm=hpicfNtpServerNameAssoIsOobm, hpicfNtpConfigPollMinInterval=hpicfNtpConfigPollMinInterval, hpicfNtpAssoSampleTable=hpicfNtpAssoSampleTable, hpicfNtpAssoXmtTimeFrac=hpicfNtpAssoXmtTimeFrac, hpicfNtpAssoRecvTimeSec=hpicfNtpAssoRecvTimeSec, hpicfNtpConfig=hpicfNtpConfig, hpicfNtpInetServerAuthKeyId=hpicfNtpInetServerAuthKeyId, hpicfNtpAuthenticationKeyTrusted=hpicfNtpAuthenticationKeyTrusted, hpicfNtpConfigPollMaxInterval=hpicfNtpConfigPollMaxInterval, hpicfNtpAssolastPollreq=hpicfNtpAssolastPollreq, hpicfNtpInetServerNameTable=hpicfNtpInetServerNameTable, hpicfNtpGlobal=hpicfNtpGlobal, hpicfNtpStatusRootDispersion=hpicfNtpStatusRootDispersion, hpicfNtpInetServerConfigGroup=hpicfNtpInetServerConfigGroup)