#
# PySNMP MIB module BAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:33:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, Gauge32, IpAddress, iso, ModuleIdentity, Counter64, Integer32, enterprises, Counter32, ObjectIdentity, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Gauge32", "IpAddress", "iso", "ModuleIdentity", "Counter64", "Integer32", "enterprises", "Counter32", "ObjectIdentity", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
basMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493))
if mibBuilder.loadTexts: basMIB.setLastUpdated('9810071330Z')
if mibBuilder.loadTexts: basMIB.setOrganization('Broadband Access Systems, Inc.')
if mibBuilder.loadTexts: basMIB.setContactInfo(' Tech Support Broadband Access Systems, Inc. 201 Forest Street Marlborough, MA 01752 USA 508-485-8200 support@basystems.com')
if mibBuilder.loadTexts: basMIB.setDescription('The MIB module defining the nodes in the Broadband Access Systems, Inc. MIB tree.')
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
    description = 'A unique value, greater than zero, for each Chassis in the managed Broadband Access System (BAS) Cluster. It is recommended that values are assigned contiguously starting from 1. The value for each Chassis must remain constant at least from one re-initialization of the BAS Cluster Manager to the next re-initialization.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 128)

class BasSlotId(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each application card slot in the managed BAS Chassis. The value for each slot must remain constant at least from one re- initialization of the network management software within the card installed in the slot to the next re-initialization.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 12)

class BasInterfaceId(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each interface in the managed BAS application card within a chassis slot. It is recommended that values are assigned contiguously starting from 1. The value for each interface ID must remain constant at least from one re-initialization of the network management software associated with the interface to the next re-initialization. Interface 1 has a special meaning, it describes a logical port on the application card within the chassis slot. The specific logical port is specified via another object of syntax BasLogicalPortId.'
    status = 'current'
    displayHint = 'd'

class BasLogicalPortId(TextualConvention, Integer32):
    description = 'A unique value, greater than zero, for each logical port in the managed BAS application card within a chassis slot. It is recommended that values are assigned contiguously starting from 1. The value for each logical port ID must remain constant at least from one re-initialization of the network management software associated with the application card to the next re-initialization. Currently two logical ports are defined, 1 ==> main processor, 2 ==> daughter card processor. The value of an object of this syntax is meaningful only when the associated object type of syntax BasInterfaceId is equal to 1.'
    status = 'current'
    displayHint = 'd'

class BasCardClass(TextualConvention, Integer32):
    description = 'A unique value for each class of card in a managed Broadband Access System (BAS) Cluster Chassis. The value for each Chassis card class must remain constant at least from one re-initialization of the network management software on the particular card to the next re-initialization.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("clusterManager", 1), ("routeServer", 2), ("forwarder", 3), ("cmts", 4), ("routeServerForwarder", 5), ("cmtsForwarder", 6), ("routeServer10100", 7), ("routeServer1000", 8), ("routeServerOC12", 9), ("forwarder10100", 10), ("forwarder1000", 11), ("forwarderOC12", 12), ("routeServerOC3", 13), ("routeServerOC48", 14), ("forwarderOC3", 15), ("forwarderOC48", 16))

class BasIfClass(TextualConvention, Integer32):
    description = 'A unique value for each interface class in the managed BAS application card within a chassis slot.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("icl", 1), ("ccl", 2), ("egress", 3))

class BasChassisType(TextualConvention, Integer32):
    description = 'A unique value for each type of chassis in a managed Broadband Access System (BAS) Cluster. The value for each Chassis type must remain constant at least from one re-initialization of the network management software on the particular card to the next re-initialization.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("cuda", 1))

class BasSubnetClass(TextualConvention, Integer32):
    description = 'A unique value for each subnet class in the DHCP Relay table.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unauthorized", 1), ("authorized", 2), ("cablemodem", 3))

basTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 3, 1))
basTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 3, 2))
basTrapChassis = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 1), BasChassisId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapChassis.setStatus('current')
if mibBuilder.loadTexts: basTrapChassis.setDescription('Used to identify a chassis.')
basTrapSlot = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 2), BasSlotId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapSlot.setStatus('current')
if mibBuilder.loadTexts: basTrapSlot.setDescription('Used to identify a slot.')
basTrapIf = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 3), BasInterfaceId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapIf.setStatus('current')
if mibBuilder.loadTexts: basTrapIf.setDescription('Used to identify an interface.')
basTrapLPort = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 4), BasLogicalPortId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapLPort.setStatus('current')
if mibBuilder.loadTexts: basTrapLPort.setDescription('Used to identify a logical port.')
basTrapCmtsCmMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 5), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCmtsCmMacAddress.setStatus('current')
if mibBuilder.loadTexts: basTrapCmtsCmMacAddress.setDescription('Used to identify a Cable Modem MacAddress.')
basTrapCmtsCmIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 6), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCmtsCmIpAddress.setStatus('current')
if mibBuilder.loadTexts: basTrapCmtsCmIpAddress.setDescription('Used to identify a Cable Modem IpAddress.')
basTrapMgmtOneIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 7), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapMgmtOneIpAddress.setStatus('current')
if mibBuilder.loadTexts: basTrapMgmtOneIpAddress.setDescription('IpAddress for management card 1')
basTrapMgmtTwoIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 8), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapMgmtTwoIpAddress.setStatus('current')
if mibBuilder.loadTexts: basTrapMgmtTwoIpAddress.setDescription('IpAddress for management card 2')
basTrapCraftIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 9), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCraftIpAddress.setStatus('current')
if mibBuilder.loadTexts: basTrapCraftIpAddress.setDescription('IpAddress for the craft port')
basTrapIclClass = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 10), BasIfClass()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapIclClass.setStatus('current')
if mibBuilder.loadTexts: basTrapIclClass.setDescription('IpAddress for the craft port')
basTrapChassisNumber = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 11), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapChassisNumber.setStatus('current')
if mibBuilder.loadTexts: basTrapChassisNumber.setDescription('IpAddress for the craft port')
basTrapCmtsCmGwAddress = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 12), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCmtsCmGwAddress.setStatus('current')
if mibBuilder.loadTexts: basTrapCmtsCmGwAddress.setDescription('Used to identify a Cable Modem Gateway IpAddress.')
basTrapCardType = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 13), BasCardClass()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapCardType.setStatus('current')
if mibBuilder.loadTexts: basTrapCardType.setDescription('Used to identify a particular card')
basTrapSubnetType = MibScalar((1, 3, 6, 1, 4, 1, 3493, 3, 1, 14), BasSubnetClass()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapSubnetType.setStatus('current')
if mibBuilder.loadTexts: basTrapSubnetType.setDescription('used to identify a DHCP relay Server type')
mibBuilder.exportSymbols("BAS-MIB", basTrapCmtsCmIpAddress=basTrapCmtsCmIpAddress, basTraps=basTraps, basTrapSubnetType=basTrapSubnetType, basCudaOC3=basCudaOC3, basTrace=basTrace, basCudaOC48=basCudaOC48, basCmConfig=basCmConfig, basAccessControl=basAccessControl, basProductId=basProductId, basAnalyzer=basAnalyzer, basCuda1000=basCuda1000, basTrapCmtsCmMacAddress=basTrapCmtsCmMacAddress, basMIB=basMIB, BasChassisType=BasChassisType, basCuda10100Rs=basCuda10100Rs, BasIfClass=BasIfClass, basExtIp=basExtIp, basTrapObjects=basTrapObjects, basTrapGroup=basTrapGroup, basPbrfFilter=basPbrfFilter, basCudaCMTS1=basCudaCMTS1, basHackedInfo=basHackedInfo, basAliasSnmp=basAliasSnmp, basChassisInfo=basChassisInfo, basFtd=basFtd, basMcc=basMcc, BasSlotId=BasSlotId, basExtCmts=basExtCmts, basAliasRip=basAliasRip, basCudaOC12=basCudaOC12, basAliasTcp=basAliasTcp, basTrapMgmtOneIpAddress=basTrapMgmtOneIpAddress, basAliasUdp=basAliasUdp, basTrapCmtsCmGwAddress=basTrapCmtsCmGwAddress, basPbrfOSPF=basPbrfOSPF, basCudaOC12Rs=basCudaOC12Rs, BasCardClass=BasCardClass, basCudaOC3Rs=basCudaOC3Rs, basCudaOC48Rs=basCudaOC48Rs, basDhcpRelay=basDhcpRelay, basCluster=basCluster, basTrapCardType=basTrapCardType, basStartup=basStartup, basHackedAccessControl=basHackedAccessControl, basAliasOspf=basAliasOspf, basExtIf=basExtIf, basAlias=basAlias, basSonet=basSonet, basCuda10100=basCuda10100, basRip=basRip, basTrapIclClass=basTrapIclClass, basAliasDocsIf=basAliasDocsIf, basTrapMgmtTwoIpAddress=basTrapMgmtTwoIpAddress, BasSubnetClass=BasSubnetClass, basTrapIf=basTrapIf, basTrapSlot=basTrapSlot, basRbp=basRbp, basAliasCidr=basAliasCidr, basTrafGen=basTrafGen, basProvInfo=basProvInfo, basPbrfRIP=basPbrfRIP, BasLogicalPortId=BasLogicalPortId, BasInterfaceId=BasInterfaceId, basExtSys=basExtSys, basAliasDocsCd=basAliasDocsCd, basTrapChassisNumber=basTrapChassisNumber, basTrapLPort=basTrapLPort, PYSNMP_MODULE_ID=basMIB, basTopology=basTopology, basExtEvent=basExtEvent, basTrapChassis=basTrapChassis, basCuda1000Rs=basCuda1000Rs, BasChassisId=BasChassisId, basMibGroup=basMibGroup, basAliasIp=basAliasIp, basCudaChassMgr=basCudaChassMgr, basAliasCmtsCfg=basAliasCmtsCfg, basTrapCraftIpAddress=basTrapCraftIpAddress, basCardInfo=basCardInfo)
