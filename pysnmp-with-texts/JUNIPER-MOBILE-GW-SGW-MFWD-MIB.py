#
# PySNMP MIB module JUNIPER-MOBILE-GW-SGW-MFWD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MOBILE-GW-SGW-MFWD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
jnxMobileGatewaySgw, = mibBuilder.importSymbols("JUNIPER-MBG-SMI", "jnxMobileGatewaySgw")
EnabledStatus, = mibBuilder.importSymbols("JUNIPER-MIMSTP-MIB", "EnabledStatus")
jnxMbgGwName, = mibBuilder.importSymbols("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, Unsigned32, Counter32, ObjectIdentity, MibIdentifier, Bits, ModuleIdentity, IpAddress, Integer32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Unsigned32", "Counter32", "ObjectIdentity", "MibIdentifier", "Bits", "ModuleIdentity", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
jnxMbgSgwMfwdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7))
if mibBuilder.loadTexts: jnxMbgSgwMfwdMib.setLastUpdated('201108041200Z')
if mibBuilder.loadTexts: jnxMbgSgwMfwdMib.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxMbgSgwMfwdMib.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxMbgSgwMfwdMib.setDescription('This module defines objects pertaining to SGW MFWD (Serving Gateway Mobile Packet Forwarding Daemon) ')
jnxMbgSgwMfwdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0))
jnxMbgSgwMfwdNotificationVars = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1))
jnxMbgSgwMfwdServicePicName = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 15))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgSgwMfwdServicePicName.setStatus('current')
if mibBuilder.loadTexts: jnxMbgSgwMfwdServicePicName.setDescription('This identifies the session-pic, in the form ms-a/b/0, where <a> is the slot and <b> could be either 0 or 1.')
jnxMbgSgwMfwdBufMemLimit = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 1, 2), Gauge32()).setUnits('percent').setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemLimit.setStatus('current')
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemLimit.setDescription('This indicates the percentage of total buffer memory being used')
jnxMbgSgwMfwdBufMemThresRaise = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0, 1)).setObjects(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"), ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdServicePicName"), ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdBufMemLimit"))
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemThresRaise.setStatus('current')
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemThresRaise.setDescription('This notification signifies that the high memory buffering threshold for MFWD has reached at the SPIC level. The gateway name, SPIC name and memory buffer threshold will be displayed.')
jnxMbgSgwMfwdBufMemThresClear = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 7, 0, 2)).setObjects(("JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwName"), ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdServicePicName"), ("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", "jnxMbgSgwMfwdBufMemLimit"))
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemThresClear.setStatus('current')
if mibBuilder.loadTexts: jnxMbgSgwMfwdBufMemThresClear.setDescription('This notification signifies that the low memory buffering threshold for MFWD has reached at the SPIC level. The gateway name, SPIC name and memory buffer threshold will be displayed.')
mibBuilder.exportSymbols("JUNIPER-MOBILE-GW-SGW-MFWD-MIB", jnxMbgSgwMfwdNotificationVars=jnxMbgSgwMfwdNotificationVars, jnxMbgSgwMfwdBufMemThresRaise=jnxMbgSgwMfwdBufMemThresRaise, jnxMbgSgwMfwdBufMemThresClear=jnxMbgSgwMfwdBufMemThresClear, jnxMbgSgwMfwdNotifications=jnxMbgSgwMfwdNotifications, PYSNMP_MODULE_ID=jnxMbgSgwMfwdMib, jnxMbgSgwMfwdMib=jnxMbgSgwMfwdMib, jnxMbgSgwMfwdBufMemLimit=jnxMbgSgwMfwdBufMemLimit, jnxMbgSgwMfwdServicePicName=jnxMbgSgwMfwdServicePicName)