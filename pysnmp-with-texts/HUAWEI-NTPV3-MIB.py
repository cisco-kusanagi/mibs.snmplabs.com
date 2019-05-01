#
# PySNMP MIB module HUAWEI-NTPV3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-NTPV3-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:47:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Integer32, NotificationType, IpAddress, Bits, Gauge32, ObjectIdentity, ModuleIdentity, TimeTicks, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Integer32", "NotificationType", "IpAddress", "Bits", "Gauge32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwNtpV3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234))
if mibBuilder.loadTexts: hwNtpV3.setLastUpdated('201009092100Z')
if mibBuilder.loadTexts: hwNtpV3.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwNtpV3.setContactInfo('VRP Team Huawei Technologies Co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwNtpV3.setDescription('The private mib file includes the general extent information of the device.hwDatacomm(25).hwNtpV3(234)')
hwNtpV3MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1))
hwNtpV3ServerIPAdd = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNtpV3ServerIPAdd.setStatus('current')
if mibBuilder.loadTexts: hwNtpV3ServerIPAdd.setDescription('IP address or domain name of the NTP server')
hwNtpV3TimeSyncPeriod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNtpV3TimeSyncPeriod.setStatus('current')
if mibBuilder.loadTexts: hwNtpV3TimeSyncPeriod.setDescription('NTP poll interval.')
hwNtpV3TimeAfterNTPCal = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNtpV3TimeAfterNTPCal.setStatus('current')
if mibBuilder.loadTexts: hwNtpV3TimeAfterNTPCal.setDescription('This node gives the current local time of the system. The unit of it is DateAndTime.')
hwNtpV3Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2))
hwNtpV3Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 1))
hwNtpV3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 1, 1)).setObjects(("HUAWEI-NTPV3-MIB", "hwNtpV3ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwNtpV3Compliance = hwNtpV3Compliance.setStatus('current')
if mibBuilder.loadTexts: hwNtpV3Compliance.setDescription('The compliance statement for systems supporting the HUAWEI-NtpV3-MIB.')
hwNtpV3Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 2))
hwNtpV3ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 2, 1)).setObjects(("HUAWEI-NTPV3-MIB", "hwNtpV3ServerIPAdd"), ("HUAWEI-NTPV3-MIB", "hwNtpV3TimeSyncPeriod"), ("HUAWEI-NTPV3-MIB", "hwNtpV3TimeAfterNTPCal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwNtpV3ObjectGroup = hwNtpV3ObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwNtpV3ObjectGroup.setDescription('The NTPV3 attribute group.')
mibBuilder.exportSymbols("HUAWEI-NTPV3-MIB", hwNtpV3Compliances=hwNtpV3Compliances, hwNtpV3Compliance=hwNtpV3Compliance, hwNtpV3ObjectGroup=hwNtpV3ObjectGroup, hwNtpV3TimeAfterNTPCal=hwNtpV3TimeAfterNTPCal, hwNtpV3=hwNtpV3, PYSNMP_MODULE_ID=hwNtpV3, hwNtpV3Groups=hwNtpV3Groups, hwNtpV3ServerIPAdd=hwNtpV3ServerIPAdd, hwNtpV3TimeSyncPeriod=hwNtpV3TimeSyncPeriod, hwNtpV3MibObjects=hwNtpV3MibObjects, hwNtpV3Conformance=hwNtpV3Conformance)
