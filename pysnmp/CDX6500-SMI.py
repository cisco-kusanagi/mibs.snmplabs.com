#
# PySNMP MIB module CDX6500-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CDX6500-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, Counter32, enterprises, ModuleIdentity, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, MibIdentifier, iso, Counter64, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Counter32", "enterprises", "ModuleIdentity", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "MibIdentifier", "iso", "Counter64", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class Counter16(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class Counter8(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500NodeMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 1))
cdx6500Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
cdx6500NMSNMPGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 1))
cdx6500NMNodeParametersGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 2))
cdx6500NMDiagnosticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 3))
cdx6500NMControlsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 4))
cdx6500NMDLSVGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 1, 5))
cdx6500CfgProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1))
cdx6500CfgGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2))
cdx6500PCTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1))
cdx6500PCTStationProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 3))
cdx6500PCTBSC3270DeviceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4))
cdx6500PCTRouterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 5))
cdx6500PCTBridgeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 6))
cdx6500PCTNCRBSCDeviceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 7))
cdx6500PCTBSTDDeviceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 8))
cdx6500StatProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1))
cdx6500StatOtherStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2))
cdx6500StatTFTPGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3))
cdx6500StatNetworkSvcsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4))
cdx6500PSTPortProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1))
cdx6500PSTStationProtocolGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 3))
cdx6500PSTRouterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 4))
cdx6500PSTBridgeGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 5))
cdx6500PSTLANConnectionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 6))
cdx6500ContWANAdaptor = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 1))
cdx6500ContTFTP = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2))
cdx6500dsdControls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 3))
cdx6500statControls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 4))
cdx6500ContSDLC = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 5))
cdx6500ContMX25 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 6))
cdx6500ContXDLC = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 7))
isgIsdnCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 19))
isgIsdnStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 2, 9))
isgIsdnCtrlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 8))
mibBuilder.exportSymbols("CDX6500-SMI", cdx6500NMNodeParametersGroup=cdx6500NMNodeParametersGroup, cdx6500Controls=cdx6500Controls, cdx6500PSTPortProtocolGroup=cdx6500PSTPortProtocolGroup, cdx6500StatTFTPGroup=cdx6500StatTFTPGroup, isgIsdnCfgGroup=isgIsdnCfgGroup, cdx6500ContTFTP=cdx6500ContTFTP, cdx6500StatNetworkSvcsGroup=cdx6500StatNetworkSvcsGroup, cdx6500NMDiagnosticsGroup=cdx6500NMDiagnosticsGroup, cdx6500PCTNCRBSCDeviceGroup=cdx6500PCTNCRBSCDeviceGroup, Counter8=Counter8, cdx6500NMControlsGroup=cdx6500NMControlsGroup, isgIsdnCtrlGroup=isgIsdnCtrlGroup, codex=codex, cdx6500PCTBSTDDeviceGroup=cdx6500PCTBSTDDeviceGroup, cdx6500ContSDLC=cdx6500ContSDLC, cdx6500PCTPortProtocolGroup=cdx6500PCTPortProtocolGroup, cdx6500PSTLANConnectionGroup=cdx6500PSTLANConnectionGroup, cdx6500dsdControls=cdx6500dsdControls, cdx6500PCTStationProtocolGroup=cdx6500PCTStationProtocolGroup, cdx6500ContWANAdaptor=cdx6500ContWANAdaptor, cdx6500NodeMgmt=cdx6500NodeMgmt, cdx6500Configuration=cdx6500Configuration, cdx6500StatProtocolGroup=cdx6500StatProtocolGroup, cdx6500PCTBridgeGroup=cdx6500PCTBridgeGroup, cdx6500PSTBridgeGroup=cdx6500PSTBridgeGroup, cdx6500PSTStationProtocolGroup=cdx6500PSTStationProtocolGroup, cdx6500Statistics=cdx6500Statistics, cdx6500ContMX25=cdx6500ContMX25, Counter16=Counter16, cdx6500PCTBSC3270DeviceGroup=cdx6500PCTBSC3270DeviceGroup, cdxProductSpecific=cdxProductSpecific, MacAddress=MacAddress, cdx6500=cdx6500, cdx6500NMSNMPGroup=cdx6500NMSNMPGroup, cdx6500NMDLSVGroup=cdx6500NMDLSVGroup, cdx6500StatOtherStatsGroup=cdx6500StatOtherStatsGroup, isgIsdnStatsGroup=isgIsdnStatsGroup, cdx6500statControls=cdx6500statControls, cdx6500PCTRouterGroup=cdx6500PCTRouterGroup, cdx6500CfgProtocolGroup=cdx6500CfgProtocolGroup, cdx6500CfgGeneralGroup=cdx6500CfgGeneralGroup, cdx6500ContXDLC=cdx6500ContXDLC, cdx6500PSTRouterGroup=cdx6500PSTRouterGroup)
