#
# PySNMP MIB module HUAWEI-NTPV3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-NTPV3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:35:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Counter64, ModuleIdentity, TimeTicks, Gauge32, Unsigned32, ObjectIdentity, Counter32, Integer32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Counter64", "ModuleIdentity", "TimeTicks", "Gauge32", "Unsigned32", "ObjectIdentity", "Counter32", "Integer32", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwNtpV3 = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234))
if mibBuilder.loadTexts: hwNtpV3.setLastUpdated('201009092100Z')
if mibBuilder.loadTexts: hwNtpV3.setOrganization('Huawei Technologies Co.,Ltd.')
hwNtpV3MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1))
hwNtpV3ServerIPAdd = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNtpV3ServerIPAdd.setStatus('current')
hwNtpV3TimeSyncPeriod = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNtpV3TimeSyncPeriod.setStatus('current')
hwNtpV3TimeAfterNTPCal = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNtpV3TimeAfterNTPCal.setStatus('current')
hwNtpV3Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2))
hwNtpV3Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 1))
hwNtpV3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 1, 1)).setObjects(("HUAWEI-NTPV3-MIB", "hwNtpV3ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwNtpV3Compliance = hwNtpV3Compliance.setStatus('current')
hwNtpV3Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 2))
hwNtpV3ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 234, 2, 2, 1)).setObjects(("HUAWEI-NTPV3-MIB", "hwNtpV3ServerIPAdd"), ("HUAWEI-NTPV3-MIB", "hwNtpV3TimeSyncPeriod"), ("HUAWEI-NTPV3-MIB", "hwNtpV3TimeAfterNTPCal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwNtpV3ObjectGroup = hwNtpV3ObjectGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-NTPV3-MIB", hwNtpV3Compliance=hwNtpV3Compliance, hwNtpV3MibObjects=hwNtpV3MibObjects, hwNtpV3Compliances=hwNtpV3Compliances, hwNtpV3TimeAfterNTPCal=hwNtpV3TimeAfterNTPCal, hwNtpV3Conformance=hwNtpV3Conformance, PYSNMP_MODULE_ID=hwNtpV3, hwNtpV3TimeSyncPeriod=hwNtpV3TimeSyncPeriod, hwNtpV3Groups=hwNtpV3Groups, hwNtpV3=hwNtpV3, hwNtpV3ServerIPAdd=hwNtpV3ServerIPAdd, hwNtpV3ObjectGroup=hwNtpV3ObjectGroup)
