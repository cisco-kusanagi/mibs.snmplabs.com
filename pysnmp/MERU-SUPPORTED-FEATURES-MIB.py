#
# PySNMP MIB module MERU-SUPPORTED-FEATURES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-SUPPORTED-FEATURES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
mwConfiguration, = mibBuilder.importSymbols("MERU-SMI", "mwConfiguration")
MwlOnOffSwitch, MwlIpProxyType = mibBuilder.importSymbols("MERU-TC", "MwlOnOffSwitch", "MwlIpProxyType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Bits, enterprises, iso, TimeTicks, Integer32, Unsigned32, MibIdentifier, Counter64, IpAddress, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Bits", "enterprises", "iso", "TimeTicks", "Integer32", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress", "ModuleIdentity", "ObjectIdentity")
TimeInterval, TextualConvention, TimeStamp, RowStatus, DisplayString, MacAddress, DateAndTime, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "TextualConvention", "TimeStamp", "RowStatus", "DisplayString", "MacAddress", "DateAndTime", "TruthValue")
mwSupportedFeatures = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14))
if mibBuilder.loadTexts: mwSupportedFeatures.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: mwSupportedFeatures.setOrganization('Meru Networks')
mwSupport = MibIdentifier((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1))
mwSupportChannelDomainCheck = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 1), MwlOnOffSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSupportChannelDomainCheck.setStatus('current')
mwSupportLicensingMgmt = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 2), MwlOnOffSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSupportLicensingMgmt.setStatus('current')
mwSupportSipProxy = MibScalar((1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 14, 1, 3), MwlIpProxyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mwSupportSipProxy.setStatus('current')
mibBuilder.exportSymbols("MERU-SUPPORTED-FEATURES-MIB", mwSupportedFeatures=mwSupportedFeatures, mwSupportLicensingMgmt=mwSupportLicensingMgmt, PYSNMP_MODULE_ID=mwSupportedFeatures, mwSupportSipProxy=mwSupportSipProxy, mwSupportChannelDomainCheck=mwSupportChannelDomainCheck, mwSupport=mwSupport)
