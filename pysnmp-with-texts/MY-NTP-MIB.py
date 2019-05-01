#
# PySNMP MIB module MY-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-NTP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:16:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, iso, Counter64, Counter32, Integer32, NotificationType, Gauge32, ModuleIdentity, TimeTicks, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "iso", "Counter64", "Counter32", "Integer32", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
myNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49))
myNtpMIB.setRevisions(('2009-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: myNtpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: myNtpMIB.setLastUpdated('200905140000Z')
if mibBuilder.loadTexts: myNtpMIB.setOrganization('D-Link Crop.')
if mibBuilder.loadTexts: myNtpMIB.setContactInfo(' http://support.dlink.com')
if mibBuilder.loadTexts: myNtpMIB.setDescription('This module defines my ntp mibs.')
myNtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1))
myNtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2))
myntpSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1))
myNtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 1))
myNtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 2))
class NTPTimeStamp(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class NTPLeapIndicator(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("noWarning", 0), ("addSecond", 1), ("subtractSecond", 2), ("alarm", 3))

class NTPSignedTimeValue(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPUnsignedTimeValue(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class NTPStratum(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class NTPRefId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

myntpSysLeap = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 1), NTPLeapIndicator()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myntpSysLeap.setStatus('mandatory')
if mibBuilder.loadTexts: myntpSysLeap.setDescription('Two-bit code warning of an impending leap second to be inserted in the NTP timescale. This object can be set only when the myntpSysStratum has a value of 1.')
myntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myntpSysStratum.setStatus('mandatory')
if mibBuilder.loadTexts: myntpSysStratum.setDescription('The stratum of the local clock. If the value is set to 1, i.e., this is a primary reference, then the Primary-Clock procedure described in Section 3.4.6, in RFC-1305 is invoked.')
myntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-24, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysPrecision.setStatus('mandatory')
if mibBuilder.loadTexts: myntpSysPrecision.setDescription('Signed integer indicating the precision of the system clock, in seconds to the nearest power of two. The value must be rounded to the next larger power of two; for instance, a 50-Hz (20 ms) or 60-Hz (16.67 ms) power-frequency clock would be assigned the value -5 (31.25 ms), while a 1000-Hz (1 ms) crystal-controlled clock would be assigned the value -9 (1.95 ms).')
myntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 4), NTPSignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRootDelay.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2.2, 3.2.1")
if mibBuilder.loadTexts: myntpSysRootDelay.setStatus('mandatory')
if mibBuilder.loadTexts: myntpSysRootDelay.setDescription('A signed fixed-point number indicating the total round-trip delay in seconds, to the primary reference source at the root of the synchronization subnet.')
myntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 5), NTPUnsignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRootDispersion.setReference("D.L. Mills, 'Network Time Protocol (Version 3)', RFC-1305, March 1992, Sections 2, 2.2, 3.2.1")
if mibBuilder.loadTexts: myntpSysRootDispersion.setStatus('mandatory')
if mibBuilder.loadTexts: myntpSysRootDispersion.setDescription('The maximum error in seconds, relative to the primary reference source at the root of the synchronization subnet. Only positive values greater than zero are possible.')
myntpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRefId.setStatus('mandatory')
if mibBuilder.loadTexts: myntpSysRefId.setDescription('The reference identifier of the local clock.')
myntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRefTime.setStatus('mandatory')
if mibBuilder.loadTexts: myntpSysRefTime.setDescription('The local time when the local clock was last updated. If the local clock has never been synchronized, the value is zero.')
myNtpSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 2, 1)).setObjects(("MY-NTP-MIB", "myntpSysLeap"), ("MY-NTP-MIB", "myntpSysStratum"), ("MY-NTP-MIB", "myntpSysPrecision"), ("MY-NTP-MIB", "myntpSysRootDelay"), ("MY-NTP-MIB", "myntpSysRootDispersion"), ("MY-NTP-MIB", "myntpSysRefId"), ("MY-NTP-MIB", "myntpSysRefTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNtpSysGroup = myNtpSysGroup.setStatus('current')
if mibBuilder.loadTexts: myNtpSysGroup.setDescription('The NTP system variables.')
myNtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 1, 1)).setObjects(("MY-NTP-MIB", "myNtpMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNtpMIBCompliance = myNtpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: myNtpMIBCompliance.setDescription('The compliance statement for agents which implement the NTP MIB.')
mibBuilder.exportSymbols("MY-NTP-MIB", NTPLeapIndicator=NTPLeapIndicator, myntpSysPrecision=myntpSysPrecision, myntpSysStratum=myntpSysStratum, NTPTimeStamp=NTPTimeStamp, myntpSysLeap=myntpSysLeap, myntpSysRootDispersion=myntpSysRootDispersion, myNtpMIB=myNtpMIB, NTPStratum=NTPStratum, myNtpSysGroup=myNtpSysGroup, myNtpMIBGroups=myNtpMIBGroups, myntpSysRootDelay=myntpSysRootDelay, myNtpMIBConformance=myNtpMIBConformance, myntpSysRefTime=myntpSysRefTime, myntpSystem=myntpSystem, myNtpMIBObjects=myNtpMIBObjects, myntpSysRefId=myntpSysRefId, NTPUnsignedTimeValue=NTPUnsignedTimeValue, NTPRefId=NTPRefId, myNtpMIBCompliances=myNtpMIBCompliances, NTPSignedTimeValue=NTPSignedTimeValue, PYSNMP_MODULE_ID=myNtpMIB, myNtpMIBCompliance=myNtpMIBCompliance)
