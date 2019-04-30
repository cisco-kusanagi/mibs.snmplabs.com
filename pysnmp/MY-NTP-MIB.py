#
# PySNMP MIB module MY-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-NTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, iso, MibIdentifier, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, NotificationType, ModuleIdentity, Unsigned32, ObjectIdentity, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "iso", "MibIdentifier", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "NotificationType", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Counter64", "IpAddress")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
myNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49))
myNtpMIB.setRevisions(('2009-05-14 00:00',))
if mibBuilder.loadTexts: myNtpMIB.setLastUpdated('200905140000Z')
if mibBuilder.loadTexts: myNtpMIB.setOrganization('D-Link Crop.')
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
myntpSysStratum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 2), NTPStratum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myntpSysStratum.setStatus('mandatory')
myntpSysPrecision = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-24, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysPrecision.setStatus('mandatory')
myntpSysRootDelay = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 4), NTPSignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRootDelay.setStatus('mandatory')
myntpSysRootDispersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 5), NTPUnsignedTimeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRootDispersion.setStatus('mandatory')
myntpSysRefId = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 6), NTPRefId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRefId.setStatus('mandatory')
myntpSysRefTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 1, 1, 7), NTPTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myntpSysRefTime.setStatus('mandatory')
myNtpSysGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 2, 1)).setObjects(("MY-NTP-MIB", "myntpSysLeap"), ("MY-NTP-MIB", "myntpSysStratum"), ("MY-NTP-MIB", "myntpSysPrecision"), ("MY-NTP-MIB", "myntpSysRootDelay"), ("MY-NTP-MIB", "myntpSysRootDispersion"), ("MY-NTP-MIB", "myntpSysRefId"), ("MY-NTP-MIB", "myntpSysRefTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNtpSysGroup = myNtpSysGroup.setStatus('current')
myNtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 49, 2, 1, 1)).setObjects(("MY-NTP-MIB", "myNtpMIBGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myNtpMIBCompliance = myNtpMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("MY-NTP-MIB", myNtpMIBObjects=myNtpMIBObjects, myntpSysRootDispersion=myntpSysRootDispersion, myNtpMIBCompliances=myNtpMIBCompliances, NTPRefId=NTPRefId, myNtpMIBConformance=myNtpMIBConformance, myntpSystem=myntpSystem, NTPLeapIndicator=NTPLeapIndicator, NTPTimeStamp=NTPTimeStamp, myntpSysStratum=myntpSysStratum, myntpSysPrecision=myntpSysPrecision, myntpSysRefTime=myntpSysRefTime, myNtpMIBGroups=myNtpMIBGroups, myntpSysLeap=myntpSysLeap, NTPStratum=NTPStratum, myntpSysRefId=myntpSysRefId, PYSNMP_MODULE_ID=myNtpMIB, myNtpMIBCompliance=myNtpMIBCompliance, myntpSysRootDelay=myntpSysRootDelay, myNtpSysGroup=myNtpSysGroup, myNtpMIB=myNtpMIB, NTPUnsignedTimeValue=NTPUnsignedTimeValue, NTPSignedTimeValue=NTPSignedTimeValue)
