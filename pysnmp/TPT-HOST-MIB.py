#
# PySNMP MIB module TPT-HOST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-HOST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, Counter64, Bits, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tpt_tpa_objs, = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs")
tpt_host_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12)).setLabel("tpt-host-objs")
tpt_host_objs.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_host_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_host_objs.setOrganization('Trend Micro, Inc.')
class EnabledOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class ActiveOrNot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inactive", 0), ("active", 1))

class IpAddressType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("iptypeIPv4", 1), ("iptypeIPv6user", 2), ("iptypeIPv6local", 3), ("iptypeIPv6auto", 4))

class FipsMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("crypto", 1), ("full", 2))

class ActiveCert(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("temporary", 1), ("authorized", 2))

class InitState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("in-progress", 0), ("complete", 1))

hostIpTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1), )
if mibBuilder.loadTexts: hostIpTable.setStatus('current')
hostIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1), ).setIndexNames((0, "TPT-HOST-MIB", "hostIpIndex"))
if mibBuilder.loadTexts: hostIpEntry.setStatus('current')
hostIpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hostIpIndex.setStatus('current')
hostIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpAddress.setStatus('current')
hostIpType = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 3), IpAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpType.setStatus('current')
hostIpActive = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 4), ActiveOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIpActive.setStatus('current')
hostIPv4Gateway = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv4Gateway.setStatus('current')
hostIPv6Gateway = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6Gateway.setStatus('current')
hostIPv6Enabled = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 4), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6Enabled.setStatus('current')
hostIPv6AutoConfig = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 5), EnabledOrNot()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIPv6AutoConfig.setStatus('current')
hostFipsCfgMode = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 6), FipsMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostFipsCfgMode.setStatus('current')
hostFipsMode = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 7), FipsMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostFipsMode.setStatus('current')
hostSSLCert = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 8), ActiveCert()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostSSLCert.setStatus('current')
hostInitState = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 9), InitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostInitState.setStatus('current')
mibBuilder.exportSymbols("TPT-HOST-MIB", hostIPv6Gateway=hostIPv6Gateway, hostFipsMode=hostFipsMode, EnabledOrNot=EnabledOrNot, hostInitState=hostInitState, hostIpAddress=hostIpAddress, hostIpTable=hostIpTable, hostIpType=hostIpType, IpAddressType=IpAddressType, hostIPv4Gateway=hostIPv4Gateway, ActiveCert=ActiveCert, PYSNMP_MODULE_ID=tpt_host_objs, hostIPv6AutoConfig=hostIPv6AutoConfig, hostIPv6Enabled=hostIPv6Enabled, ActiveOrNot=ActiveOrNot, FipsMode=FipsMode, hostSSLCert=hostSSLCert, hostIpEntry=hostIpEntry, InitState=InitState, tpt_host_objs=tpt_host_objs, hostIpActive=hostIpActive, hostIpIndex=hostIpIndex, hostFipsCfgMode=hostFipsCfgMode)
