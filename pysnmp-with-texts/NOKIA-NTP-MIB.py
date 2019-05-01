#
# PySNMP MIB module NOKIA-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-NTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ntcNtpMibs, ntcNtpReqs, ntcCommonModules = mibBuilder.importSymbols("NOKIA-COMMON-MIB-OID-REGISTRATION-MIB", "ntcNtpMibs", "ntcNtpReqs", "ntcCommonModules")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, IpAddress, iso, Counter32, Bits, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Unsigned32, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "IpAddress", "iso", "Counter32", "Bits", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Unsigned32", "NotificationType", "MibIdentifier")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
nokiaNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 2))
nokiaNtpMIB.setRevisions(('1998-10-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nokiaNtpMIB.setRevisionsDescriptions(("Rev 0.09 September 29, 1998 Initial version by K. Miettinen. Rev 0.10 September 30, 1998 MKi - ready for review. Rev 0.11 October 01, 1998 MKi - Editorial corrections. Rev 0.12 October 02, 1998 MKi - Harm. body comments included. Rev 0.13 October 07, 1998 MKi - Rest of the comments included. Rev 0.14 October 07, 1998 MKi - KMi's 'Final' comments included. Rev 0.15 August 05, 1999 AKL - Reference to ntcNtpModule changed reference to ntcCommonModules 2. Some IMPORTS not used removed and ntcCommonMOdules imported",))
if mibBuilder.loadTexts: nokiaNtpMIB.setLastUpdated('9908050000Z')
if mibBuilder.loadTexts: nokiaNtpMIB.setOrganization('Nokia')
if mibBuilder.loadTexts: nokiaNtpMIB.setContactInfo('Anna-Kaisa Lindfors Nokia Telecommunications Oy P.O.Box 315, FIN-00045 NOKIA GROUP, Finland +358-1-511 21 anna-kaisa.lindfors@ntc.nokia.com')
if mibBuilder.loadTexts: nokiaNtpMIB.setDescription("This MIB module defines management objects that model the management aspects of real time clocks, including NTP client. This includes status and configuration information. This work is partially derived from the 'Management of the Network Time Protocol (NTP) with SNMP' MIB by Adarshpal S. Sethi, Hongxiang Gao, and David Mills.")
nokiaNtpObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1))
ntcNtpConf = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1))
ntcNtpRtcConf = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2))
ntcNtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1))
ntcNtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 2))
class EnabledDisabled(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TimeServerStatus(TextualConvention, Integer32):
    description = "Current status of the corresponding NTP server or NE's capability to communicate with the NTP server. Value ok(1) means that NE is able to communicate with this NTP server, value notReachable(2) means that this NTP server is not reachable, value clockNotInSynch(3) means that this NTP server is currently unsynchronized (has just come up, has been too long without external time source or its clock has been reset), value diffTooBig(4)means that the NE cannot synchronize with this NTP server because the difference between NTP server and NE's RTC is too big (> 1000 seconds), and value otherError(5) is reserved for any other errors."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ok", 1), ("notReachable", 2), ("clockNotInSynch", 3), ("diffTooBig", 4), ("otherError", 5))

ntcNtpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 1), EnabledDisabled()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcNtpEnabled.setStatus('current')
if mibBuilder.loadTexts: ntcNtpEnabled.setDescription("Used to determine if the NE is using NTP (Network Time Protocol) to update it's internal RTC. Possible values are 'enabled' (1) and 'disabled' (2), and the NTP is turned on or off according to this setting. If the variable is set to 'enabled' (1) while it is already 'enabled' (1), then program implementing NTP (e.g. xntpd) is restarted.")
ntcNtpServerTableNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcNtpServerTableNextIndex.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerTableNextIndex.setDescription('Reading this variable returns an available index for row creation in ntcNtpServerTable. Subsequent reads should not return same values to avoid conflicts in multiple manager cases. The value zero indicates that no unassigned entries are available.')
ntcNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3), )
if mibBuilder.loadTexts: ntcNtpServerTable.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerTable.setDescription('The list of NTP servers available for this network element.')
ntcNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1), ).setIndexNames((0, "NOKIA-NTP-MIB", "ntcNtpServerIndex"))
if mibBuilder.loadTexts: ntcNtpServerEntry.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerEntry.setDescription('The data for one NTP server.')
ntcNtpServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ntcNtpServerIndex.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerIndex.setDescription('A unique value, greater than zero, for each NTP server. It is recommended that values are assigned continuously starting from 1.')
ntcNtpServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ntcNtpServerAddress.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerAddress.setDescription('Address from which NTP based time is requested. This can be either absolute IP address eg. 131.228.32.41, or host name eg. ntpserver1.ntc.nokia.com.')
ntcNtpServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ntcNtpServerPort.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerPort.setDescription('Port number used in NTP communication with NTP server. The default value of this variable shall be 123.')
ntcNtpServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 4), TimeServerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcNtpServerStatus.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerStatus.setDescription("Current status of the corresponding NTP server or NE's capability to communicate with the NTP server. ")
ntcNtpServerPreferred = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ntcNtpServerPreferred.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerPreferred.setDescription("This boolean variable marks the server as preferred ('true' (1)) or non-preferred ('false' (2)).")
ntcNtpServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ntcNtpServerRowStatus.setStatus('current')
if mibBuilder.loadTexts: ntcNtpServerRowStatus.setDescription('This object is used to create new rows in this table, modify existing rows, and to delete existing rows. For further details see RowStatus defined in RFC1903')
ntcNtpRtcCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcNtpRtcCurrentTime.setStatus('current')
if mibBuilder.loadTexts: ntcNtpRtcCurrentTime.setDescription('Reading this variable gives the current local time of NEs RTC including the time zone information. NEs local time can be set by updating this variable. The time is always returned and must be always set in a format of full 11 octects as DateAndTime in RFC 1514, as follows: octets contents range 1-2 year 0..65536 (in network byte order) 3 month 1..12 4 day 1..31 5 hour 0..23 6 minutes 0..59 7 seconds 0..60 (use 60 for leap-second) 8 deci-seconds 0..9 9 direction from UTC + or - (in ascii notation) 10 hours from UTC 0..13 11 minutes from UTC 0..59')
ntcNtpRtcTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcNtpRtcTimeZone.setStatus('current')
if mibBuilder.loadTexts: ntcNtpRtcTimeZone.setDescription('Reading this variable gives the time zone where the NE is located. NEs time zone can be set by updating this variable. If the first character is + or - then the variable is interpreted as the direction from UTC (+ means east from UTC and - means west from UTC), and the next 4 characters are the hours and minutes values of the timezone (eg. +0300). Otherwise the string is an implementation specific name of the timezone (eg. EET, Europe/Helsinki or GMT+3).')
nokiaNtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 2, 1)).setObjects(("NOKIA-NTP-MIB", "ntcNtpMinimumRTCGroup"), ("NOKIA-NTP-MIB", "ntcNtpMandatoryNTPGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nokiaNtpCompliance = nokiaNtpCompliance.setStatus('current')
if mibBuilder.loadTexts: nokiaNtpCompliance.setDescription('Describes the requirements for conformance to the Nokia NTP MIB')
ntcNtpMinimumRTCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1, 1)).setObjects(("NOKIA-NTP-MIB", "ntcNtpRtcCurrentTime"), ("NOKIA-NTP-MIB", "ntcNtpRtcTimeZone"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcNtpMinimumRTCGroup = ntcNtpMinimumRTCGroup.setStatus('current')
if mibBuilder.loadTexts: ntcNtpMinimumRTCGroup.setDescription('All of these objects are required to be implemented if Real Time Clock is implemented.')
ntcNtpMandatoryNTPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1, 2)).setObjects(("NOKIA-NTP-MIB", "ntcNtpEnabled"), ("NOKIA-NTP-MIB", "ntcNtpServerTableNextIndex"), ("NOKIA-NTP-MIB", "ntcNtpServerAddress"), ("NOKIA-NTP-MIB", "ntcNtpServerPort"), ("NOKIA-NTP-MIB", "ntcNtpServerStatus"), ("NOKIA-NTP-MIB", "ntcNtpServerPreferred"), ("NOKIA-NTP-MIB", "ntcNtpServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcNtpMandatoryNTPGroup = ntcNtpMandatoryNTPGroup.setStatus('current')
if mibBuilder.loadTexts: ntcNtpMandatoryNTPGroup.setDescription('All of these objects are required to be implemented if NTP is supported.')
mibBuilder.exportSymbols("NOKIA-NTP-MIB", nokiaNtpMIB=nokiaNtpMIB, ntcNtpRtcConf=ntcNtpRtcConf, ntcNtpCompliances=ntcNtpCompliances, ntcNtpRtcTimeZone=ntcNtpRtcTimeZone, ntcNtpMandatoryNTPGroup=ntcNtpMandatoryNTPGroup, ntcNtpEnabled=ntcNtpEnabled, ntcNtpServerIndex=ntcNtpServerIndex, nokiaNtpCompliance=nokiaNtpCompliance, ntcNtpServerStatus=ntcNtpServerStatus, EnabledDisabled=EnabledDisabled, ntcNtpRtcCurrentTime=ntcNtpRtcCurrentTime, ntcNtpConf=ntcNtpConf, ntcNtpServerRowStatus=ntcNtpServerRowStatus, TimeServerStatus=TimeServerStatus, ntcNtpServerPort=ntcNtpServerPort, ntcNtpServerAddress=ntcNtpServerAddress, nokiaNtpObjs=nokiaNtpObjs, ntcNtpServerTable=ntcNtpServerTable, ntcNtpMinimumRTCGroup=ntcNtpMinimumRTCGroup, ntcNtpServerEntry=ntcNtpServerEntry, ntcNtpGroups=ntcNtpGroups, ntcNtpServerPreferred=ntcNtpServerPreferred, PYSNMP_MODULE_ID=nokiaNtpMIB, ntcNtpServerTableNextIndex=ntcNtpServerTableNextIndex)
