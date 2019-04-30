#
# PySNMP MIB module BAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:17:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, enterprises, Unsigned32, Bits, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter32, Gauge32, iso, IpAddress, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Unsigned32", "Bits", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter32", "Gauge32", "iso", "IpAddress", "TimeTicks", "Counter64")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
basMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493))
if mibBuilder.loadTexts: basMIB.setLastUpdated('9810071330Z')
if mibBuilder.loadTexts: basMIB.setOrganization('Broadband Access Systems, Inc.')
basProductId = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 1))
basCudaChassMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 4))
basCuda10100Rs = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 5))
basCuda1000Rs = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 6))
basCudaOC12Rs = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 7))
basCuda10100 = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 8))
basCuda1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 9))
basCudaOC12 = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 10))
basCudaCMTS1 = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 11))
basCudaOC3Rs = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 12))
basCudaOC48Rs = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 13))
basCudaOC3 = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 14))
basCudaOC48 = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 15))
basMibGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2))
basTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 3))
basExtSys = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1))
basExtIf = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 2))
basExtIp = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 3))
basExtCmts = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 4))
basFtd = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 5))
basRbp = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 6))
basAlias = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7))
basExtEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 8))
basTopology = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 9))
basAccessControl = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 10))
basPbrfFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 11))
basCmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 12))
basTrafGen = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 13))
basTrace = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 14))
basDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 15))
basMcc = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 16))
basAnalyzer = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 17))
basCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 18))
basRip = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 19))
basSonet = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 20))
basStartup = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 1))
basCardInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 2))
basChassisInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 3))
basProvInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4))
basHackedInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 1000))
basHackedAccessControl = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1001))
basAliasSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 1))
basAliasIp = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 2))
basAliasTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 3))
basAliasUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 4))
basAliasCidr = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 5))
basAliasRip = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 6))
basAliasOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 7))
basAliasDocsIf = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 8))
basAliasDocsCd = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 9))
basAliasCmtsCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 7, 10))
basPbrfRIP = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 11, 1))
basPbrfOSPF = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 11, 2))
class BasChassisId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 128)

class BasSlotId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 12)

class BasInterfaceId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class BasLogicalPortId(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'

class BasCardClass(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("clusterManager", 1), ("routeServer", 2), ("forwarder", 3), ("cmts", 4), ("routeServerForwarder", 5), ("cmtsForwarder", 6), ("routeServer10100", 7), ("routeServer1000", 8), ("routeServerOC12", 9), ("forwarder10100", 10), ("forwarder1000", 11), ("forwarderOC12", 12), ("routeServerOC3", 13), ("routeServerOC48", 14), ("forwarderOC3", 15), ("forwarderOC48", 16))

class BasIfClass(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("icl", 1), ("ccl", 2), ("egress", 3))

class BasChassisType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("cuda", 1))

class BasSubnetClass(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unauthorized", 1), ("authorized", 2), ("cablemodem", 3))

basTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 3, 1))
basTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 3, 2))
basTrapChassis = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 1), BasChassisId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapChassis.setStatus('current')
basTrapSlot = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 2), BasSlotId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapSlot.setStatus('current')
basTrapIf = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 3), BasInterfaceId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapIf.setStatus('current')
basTrapLPort = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 4), BasLogicalPortId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapLPort.setStatus('current')
basTrapCmtsCmMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 5), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCmtsCmMacAddress.setStatus('current')
basTrapCmtsCmIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 6), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCmtsCmIpAddress.setStatus('current')
basTrapMgmtOneIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 7), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapMgmtOneIpAddress.setStatus('current')
basTrapMgmtTwoIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 8), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapMgmtTwoIpAddress.setStatus('current')
basTrapCraftIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 9), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCraftIpAddress.setStatus('current')
basTrapIclClass = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 10), BasIfClass()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapIclClass.setStatus('current')
basTrapChassisNumber = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapChassisNumber.setStatus('current')
basTrapCmtsCmGwAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 12), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCmtsCmGwAddress.setStatus('current')
basTrapCardType = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 13), BasCardClass()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCardType.setStatus('current')
basTrapSubnetType = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 14), BasSubnetClass()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapSubnetType.setStatus('current')
mibBuilder.exportSymbols("BAS-MIB", basCudaOC12=basCudaOC12, basExtSys=basExtSys, basChassisInfo=basChassisInfo, basRbp=basRbp, basExtCmts=basExtCmts, PYSNMP_MODULE_ID=basMIB, basSonet=basSonet, basTrapChassisNumber=basTrapChassisNumber, basAliasUdp=basAliasUdp, basTrapIf=basTrapIf, basAliasRip=basAliasRip, basAliasSnmp=basAliasSnmp, basMIB=basMIB, basExtEvent=basExtEvent, BasIfClass=BasIfClass, basAlias=basAlias, basMibGroup=basMibGroup, basHackedInfo=basHackedInfo, BasChassisType=BasChassisType, basTrapCmtsCmIpAddress=basTrapCmtsCmIpAddress, basProvInfo=basProvInfo, basTrapObjects=basTrapObjects, basPbrfFilter=basPbrfFilter, basCudaOC48Rs=basCudaOC48Rs, basTrapGroup=basTrapGroup, basStartup=basStartup, basAliasTcp=basAliasTcp, basCmConfig=basCmConfig, BasChassisId=BasChassisId, BasLogicalPortId=BasLogicalPortId, basExtIp=basExtIp, basCuda1000Rs=basCuda1000Rs, basCuda10100Rs=basCuda10100Rs, basTrapCraftIpAddress=basTrapCraftIpAddress, basAliasCmtsCfg=basAliasCmtsCfg, basCudaOC3=basCudaOC3, basCuda10100=basCuda10100, basTrapCardType=basTrapCardType, basCudaOC48=basCudaOC48, basCuda1000=basCuda1000, basAnalyzer=basAnalyzer, basCluster=basCluster, BasInterfaceId=BasInterfaceId, basProductId=basProductId, BasSubnetClass=BasSubnetClass, basHackedAccessControl=basHackedAccessControl, basAliasIp=basAliasIp, basCudaOC3Rs=basCudaOC3Rs, basPbrfOSPF=basPbrfOSPF, basTrace=basTrace, basTrapIclClass=basTrapIclClass, basExtIf=basExtIf, basCudaChassMgr=basCudaChassMgr, basTrapMgmtOneIpAddress=basTrapMgmtOneIpAddress, basTrapCmtsCmGwAddress=basTrapCmtsCmGwAddress, basTrapSubnetType=basTrapSubnetType, basTrafGen=basTrafGen, basRip=basRip, basTrapChassis=basTrapChassis, basTrapLPort=basTrapLPort, basTrapMgmtTwoIpAddress=basTrapMgmtTwoIpAddress, BasSlotId=BasSlotId, basAliasCidr=basAliasCidr, basTraps=basTraps, basCudaOC12Rs=basCudaOC12Rs, basFtd=basFtd, basPbrfRIP=basPbrfRIP, basTrapCmtsCmMacAddress=basTrapCmtsCmMacAddress, basCardInfo=basCardInfo, basMcc=basMcc, basAliasOspf=basAliasOspf, basDhcpRelay=basDhcpRelay, basTrapSlot=basTrapSlot, basAccessControl=basAccessControl, basAliasDocsCd=basAliasDocsCd, BasCardClass=BasCardClass, basAliasDocsIf=basAliasDocsIf, basTopology=basTopology, basCudaCMTS1=basCudaCMTS1)
