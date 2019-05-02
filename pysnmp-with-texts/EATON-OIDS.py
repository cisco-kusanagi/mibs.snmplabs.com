#
# PySNMP MIB module EATON-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EATON-OIDS
# Produced by pysmi-0.3.4 at Wed May  1 12:59:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, ModuleIdentity, IpAddress, MibIdentifier, ObjectIdentity, Bits, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, TimeTicks, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "ModuleIdentity", "IpAddress", "MibIdentifier", "ObjectIdentity", "Bits", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "TimeTicks", "NotificationType", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eaton = ModuleIdentity((1, 3, 6, 1, 4, 1, 534))
eaton.setRevisions(('2014-02-19 00:00', '2010-01-24 00:00', '2009-06-18 00:00', '2007-08-06 00:00', '2007-07-05 00:00', '2006-10-15 00:00', '2006-05-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eaton.setRevisionsDescriptions(('Added assignments for stsMIB.', 'Added assignments for eatonEpdu and eatonEpduMa.', 'Added assignments for powerCmnd and OSDCIIMIB.', 'Added assignments for pcdMIB and pxmMIB. Added common Textual Conventions for Integers.', 'Added assignment for eatonEpduMIB. Cleaned up file for public consumption.', 'Added assignments for powerChain and pxgMIB.', 'Revised from the original assignments in XUPS-MIB.txt. Note that enterprises.534. was originally assigned to Exide Electronics before Powerware was acquired by Eaton.',))
if mibBuilder.loadTexts: eaton.setLastUpdated('201402190000Z')
if mibBuilder.loadTexts: eaton.setOrganization('Eaton Corporation')
if mibBuilder.loadTexts: eaton.setContactInfo('Eaton Power Quality Technical Support (PQTS) group www.eaton.com/powerxpert Technical Resource Center phone numbers United States: 1.800.843.9433 or 919.870.3028 Canada: 1.800.461.9166 ext. 260 All other countries: Call your local service representative.')
if mibBuilder.loadTexts: eaton.setDescription("Assigns major branches from the root of Eaton's OID tree (534). Copyright (C) Exide Electronics 1992-98 Copyright (C) Powerware Corporation 1999-2004 Copyright (C) Eaton Corporation (2005-).")
xupsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 1))
xupsEnvironment = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 1, 6))
xupsObjectId = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2))
powerwareEthernetSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 1))
powerwareNetworkSnmpAdapterEther = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 2))
powerwareNetworkSnmpAdapterToken = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 3))
onlinetDaemon = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 4))
connectUPSAdapterEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 5))
powerwareNetworkDigitalIOEther = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 6))
connectUPSAdapterTokenRing = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 7))
simpleSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 8))
powerwareEliSnmpAdapter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 9))
powerwareBasicEmbeddedEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 10))
eatonPowerChainGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 11))
eatonPowerChainDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 12))
eatonPowerXpertMeter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 2, 13))
xupsIoMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 3))
powerVision = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 4))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6))
pduAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6))
hdpdu = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 2))
eatonPdu = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 6, 4))
dataCenter = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 7))
environmentalMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 6, 7, 1))
itProjects = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 7))
pki = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 7, 1))
powerChain = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 8))
powerCmnd = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 9))
sts = MibIdentifier((1, 3, 6, 1, 4, 1, 534, 10))
class PositiveInteger(TextualConvention, Integer32):
    description = 'This data type is a non-zero and non-negative value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class NonNegativeInteger(TextualConvention, Integer32):
    description = 'This data type is a non-negative value.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

mibBuilder.exportSymbols("EATON-OIDS", itProjects=itProjects, connectUPSAdapterEthernet=connectUPSAdapterEthernet, products=products, environmentalMonitor=environmentalMonitor, powerwareNetworkDigitalIOEther=powerwareNetworkDigitalIOEther, pduAgent=pduAgent, powerwareEthernetSnmpAdapter=powerwareEthernetSnmpAdapter, connectUPSAdapterTokenRing=connectUPSAdapterTokenRing, eatonPowerChainGateway=eatonPowerChainGateway, powerwareBasicEmbeddedEthernet=powerwareBasicEmbeddedEthernet, xupsObjectId=xupsObjectId, powerChain=powerChain, simpleSnmpAdapter=simpleSnmpAdapter, hdpdu=hdpdu, NonNegativeInteger=NonNegativeInteger, powerwareEliSnmpAdapter=powerwareEliSnmpAdapter, PositiveInteger=PositiveInteger, powerCmnd=powerCmnd, powerVision=powerVision, onlinetDaemon=onlinetDaemon, sts=sts, powerwareNetworkSnmpAdapterEther=powerwareNetworkSnmpAdapterEther, eatonPowerXpertMeter=eatonPowerXpertMeter, dataCenter=dataCenter, eaton=eaton, pki=pki, xupsEnvironment=xupsEnvironment, eatonPdu=eatonPdu, eatonPowerChainDevice=eatonPowerChainDevice, xupsMIB=xupsMIB, PYSNMP_MODULE_ID=eaton, xupsIoMIB=xupsIoMIB, powerwareNetworkSnmpAdapterToken=powerwareNetworkSnmpAdapterToken)
