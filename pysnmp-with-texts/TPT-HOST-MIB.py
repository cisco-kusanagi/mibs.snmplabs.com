#
# PySNMP MIB module TPT-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-HOST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Unsigned32, MibIdentifier, Bits, Integer32, NotificationType, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Unsigned32", "MibIdentifier", "Bits", "Integer32", "NotificationType", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_host_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12)).setLabel("tpt-host-objs")
tpt_host_objs.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_host_objs.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_host_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_host_objs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_host_objs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_host_objs.setDescription("Host information for the management port on the device. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class EnabledOrNot(TextualConvention, Integer32):
    description = 'An indication of whether a feature is configured as enabled or disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class ActiveOrNot(TextualConvention, Integer32):
    description = 'An indication of whether an IP address is active or inactive.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inactive", 0), ("active", 1))

class IpAddressType(TextualConvention, Integer32):
    description = 'The type of an IP address (IPv4, IPv6 user configured, IPv6 link local, or IPv6 autoconfig).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("iptypeIPv4", 1), ("iptypeIPv6user", 2), ("iptypeIPv6local", 3), ("iptypeIPv6auto", 4))

class FipsMode(TextualConvention, Integer32):
    description = 'The type of FIPS mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("crypto", 1), ("full", 2))

class ActiveCert(TextualConvention, Integer32):
    description = 'The type of active cert.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("temporary", 1), ("authorized", 2))

class InitState(TextualConvention, Integer32):
    description = 'The state of initialization.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("in-progress", 0), ("complete", 1))

hostIpTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1), )
if mibBuilder.loadTexts: hostIpTable.setStatus('current')
if mibBuilder.loadTexts: hostIpTable.setDescription('Table of IP addresses on the device and their attributes.')
hostIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1), ).setIndexNames((0, "TPT-HOST-MIB", "hostIpIndex"))
if mibBuilder.loadTexts: hostIpEntry.setStatus('current')
if mibBuilder.loadTexts: hostIpEntry.setDescription('An entry in the host IP address table. Rows cannot be created or deleted.')
hostIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hostIpIndex.setStatus('current')
if mibBuilder.loadTexts: hostIpIndex.setDescription('Index into the IP address table, starting with 1.')
hostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpAddress.setStatus('current')
if mibBuilder.loadTexts: hostIpAddress.setDescription('String representation of an IP address, in CIDR format.')
hostIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 3), IpAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpType.setStatus('current')
if mibBuilder.loadTexts: hostIpType.setDescription('Whether this IP address is IPv4 or IPv6 and how it was configured.')
hostIpActive = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 4), ActiveOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpActive.setStatus('current')
if mibBuilder.loadTexts: hostIpActive.setDescription('Whether this IP address is active.')
hostIPv4Gateway = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv4Gateway.setStatus('current')
if mibBuilder.loadTexts: hostIPv4Gateway.setDescription('The IPv4 default gateway.')
hostIPv6Gateway = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6Gateway.setStatus('current')
if mibBuilder.loadTexts: hostIPv6Gateway.setDescription('The IPv6 default gateway.')
hostIPv6Enabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 4), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6Enabled.setStatus('current')
if mibBuilder.loadTexts: hostIPv6Enabled.setDescription('Whether IPv6 is enabled on the device.')
hostIPv6AutoConfig = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 5), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6AutoConfig.setStatus('current')
if mibBuilder.loadTexts: hostIPv6AutoConfig.setDescription('Whether IPv6 autoconfig is enabled on the device.')
hostFipsCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 6), FipsMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostFipsCfgMode.setStatus('current')
if mibBuilder.loadTexts: hostFipsCfgMode.setDescription('The configured FIPS mode.')
hostFipsMode = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 7), FipsMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostFipsMode.setStatus('current')
if mibBuilder.loadTexts: hostFipsMode.setDescription('The currently active FIPS mode.')
hostSSLCert = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 8), ActiveCert()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostSSLCert.setStatus('current')
if mibBuilder.loadTexts: hostSSLCert.setDescription('The currently active SSL cert.')
hostInitState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 9), InitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInitState.setStatus('current')
if mibBuilder.loadTexts: hostInitState.setDescription('The current host initialization state.')
mibBuilder.exportSymbols("TPT-HOST-MIB", tpt_host_objs=tpt_host_objs, ActiveCert=ActiveCert, hostIPv6AutoConfig=hostIPv6AutoConfig, EnabledOrNot=EnabledOrNot, hostInitState=hostInitState, hostIpEntry=hostIpEntry, hostSSLCert=hostSSLCert, hostIPv6Gateway=hostIPv6Gateway, hostIpActive=hostIpActive, hostFipsCfgMode=hostFipsCfgMode, InitState=InitState, hostIpTable=hostIpTable, hostIpIndex=hostIpIndex, IpAddressType=IpAddressType, hostFipsMode=hostFipsMode, ActiveOrNot=ActiveOrNot, FipsMode=FipsMode, hostIpType=hostIpType, PYSNMP_MODULE_ID=tpt_host_objs, hostIpAddress=hostIpAddress, hostIPv6Enabled=hostIPv6Enabled, hostIPv4Gateway=hostIPv4Gateway)
