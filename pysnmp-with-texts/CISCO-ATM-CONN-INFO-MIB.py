#
# PySNMP MIB module CISCO-ATM-CONN-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ATM-CONN-INFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, NotificationType, ModuleIdentity, Bits, iso, ObjectIdentity, IpAddress, MibIdentifier, Counter32, Unsigned32, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "Bits", "iso", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "Unsigned32", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmConnInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9999))
ciscoAtmConnInfoMIB.setRevisions(('2003-06-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setRevisionsDescriptions(('Initial version of the MIB.',))
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setLastUpdated('200306160000Z')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setDescription('The MIB module for providing the parameters configured on an ATM interface. Terminologies used: SVC : Switched Virtual Channel SPVC : Soft Permanent Virtual Circuit SPVP : Soft Permanent Virtual Path SVPC : Switched Virtual Path Connection DAX : Connection with endpoints on the same ATM switch P2p : Point-to-point connection P2mp : Point-to-multi-point connection Root : The root of point-to-multipoint connection, which is associated with a VPI/VCI Leaf : Usually one point-to-multipoint connection consists of one root and one or more leaves. Leaf is the branch point for point to multipoint connection that is associated with a VPI/VCI Party: One or more party is associated with each leaf, all parties are associated with the same VPI/VCI that its leaf belongs to Source Via Node Destination ------- ------- ------- A| |B C| |D E| |F --+-----+----------+-----+------------+-----+-- | | | | | | ------- ------- ------- Each active connection has two terminating endpoints. In the above diagram, Endpoints A and F are terminating. Of these the master endpoint of the connection initiates the routing of the call and is considered the calling party. The slave endpoint is the called party which receives calls and is the destination of a call. Any endpoints that are created either on Via nodes or on the node with the terminating endpoint in order to have a complete connections between endpoints A and F are said to be intermediate endpoints. In the above diagram, endpoints B, C, D and E are intermediate endpoints. ')
caciMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 0))
caciMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1))
caciAtmConnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1))
caciIfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1))
caciP2pConns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2))
caciP2pEndpoints = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3))
caciP2pIntEndpoints = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4))
caciP2mpConns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5))
caciGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6))
class CaciGeneralConnEPCategory(TextualConvention, Integer32):
    description = 'General category for connection or endpoint types supported on the switch. caciP2p : Point to point connection caciP2mpR : Point to multi point root connection caciP2mpL : Point to multi point leaf connection caciP2mpPty: Point to multi point party connection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciP2p", 1), ("caciP2mpR", 2), ("caciP2mpL", 3), ("caciP2mpPty", 4))

class CaciP2pConnCategory(TextualConvention, Integer32):
    description = 'The connection category. caciP2pSvcc : Point to point Svc connection caciP2pSvpc : Point to point Svpc connection caciP2pSpvcD: Point to point Spvc DAX connection caciP2pSpvpD: Point to point Spvp DAX connection caciP2pSpvcR: Point to point SPVC Routed connection caciP2pSpvpR: Point to point Spvp Routed connection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("caciP2pSvcc", 1), ("caciP2pSvpc", 2), ("caciP2pSpvcD", 3), ("caciP2pSpvpD", 4), ("caciP2pSpvcR", 5), ("caciP2pSpvpR", 6))

class CaciP2pEndpointCategory(TextualConvention, Integer32):
    description = 'The terminating endpoint category. caciP2pSpvcRPEP : Point to point Spvc Routed Persistent endpoint caciP2pSpvcRNPEP: Point to point Spvc Routed Non-persistent endpoint caciP2pSpvpRPEP : Point to point Spvp Routed Persistent endpoint caciP2pSpvpRNPEP: Point to point Spvp Routed Non-persistent endpoint caciP2pSpvcDEP : Point to point Spvc DAX endpoint caciP2pSpvpDEP : Point to point Spvp DAX endpoint'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("caciP2pSpvcRPEP", 1), ("caciP2pSpvcRNPEP", 2), ("caciP2pSpvpRPEP", 3), ("caciP2pSpvpRNPEP", 4), ("caciP2pSpvcDEP", 5), ("caciP2pSpvpDEP", 6))

class CaciP2pIntEndpointCategory(TextualConvention, Integer32):
    description = 'The intermediate endpoint category. caciP2pSvccIntEP : Point to point Svc intermediate endpoint caciP2pSvpcIntEP : Point to point Svpc intermediate endpoint caciP2pSpvcRIntEP: Point to point Spvc Routed intermediate endpoint caciP2pSpvpRIntEP: Point to point Spvp Routed intermediate endpoint'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciP2pSvccIntEP", 1), ("caciP2pSvpcIntEP", 2), ("caciP2pSpvcRIntEP", 3), ("caciP2pSpvpRIntEP", 4))

class CaciP2mpConnCategory(TextualConvention, Integer32):
    description = 'The point to multipoint connection category. caciP2mpSvcRoot : Point to multipoint Svc root connection caciP2mpSvcLeaf : Point to multipoint Svc leaf connection caciP2mpSvcParty : Point to multipoint Svc party connection caciP2mpSvpcRoot : Point to multipoint Svpc root connection caciP2mpSvpcLeaf : Point to multipoint Svpc leaf connection caciP2mpSvpcParty: Point to multipoint Svpc party connection caciP2mpSpvcP : Point to multipoint Spvc persistent connection caciP2mpSpvcNP : Point to multipoint Spvc non-persistent connection caciP2mpSpvcAct : Point to multipoint Spvc Active connection caciP2mpSpvpP : Point to multipoint Spvp persistent connection caciP2mpSpvpNP : Point to multipoint Spvp non-persistent connection caciP2mpSpvpAct : Point to multipoint Spvp active connection caciP2mpSpvcPaP : Point to multipoint Spvc party persistent connection caciP2mpSpvcPaAct: Point to multipoint Spvc party active connection caciP2mpSpvpPaP : Point to multipoint Spvp party persistent connection caciP2mpSpvpPaAct: Point to multipoint Spvp party active connection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("caciP2mpSvcRoot", 1), ("caciP2mpSvcLeaf", 2), ("caciP2mpSvcParty", 3), ("caciP2mpSvpcRoot", 4), ("caciP2mpSvpcLeaf", 5), ("caciP2mpSvpcParty", 6), ("caciP2mpSpvcP", 7), ("caciP2mpSpvcNP", 8), ("caciP2mpSpvcAct", 9), ("caciP2mpSpvpP", 10), ("caciP2mpSpvpNP", 11), ("caciP2mpSpvpAct", 12), ("caciP2mpSpvcPaP", 13), ("caciP2mpSpvcPaAct", 14), ("caciP2mpSpvpPaP", 15), ("caciP2mpSpvpPaAct", 16))

class CaciATMEndpointCategory(TextualConvention, Integer32):
    description = 'The connection category. caciTotalSpvc : Total SPVC endpoints configured on the ATM switch caciP2pTotalInt : Total intermediate endpoints configured on the ATM switch caciTotalMaster : Total master endpoints configured on the ATM switch caciTotalSlave : Total slave endpoints configured on the ATM switch'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciTotalSpvc", 1), ("caciP2pTotalInt", 2), ("caciTotalMaster", 3), ("caciTotalSlave", 4))

caciP2pTotalConfConns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConfConns.setStatus('current')
if mibBuilder.loadTexts: caciP2pTotalConfConns.setDescription('This object specifies the total point to point connections that are configured on this ATM switch.')
caciP2pMaxPossibleConns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pMaxPossibleConns.setStatus('current')
if mibBuilder.loadTexts: caciP2pMaxPossibleConns.setDescription('This object specifies the upper limit of the point to point and point to multipoint connections that are allowed to be configured on this ATM switch.')
caciMaxPossibleEndpoints = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciMaxPossibleEndpoints.setStatus('current')
if mibBuilder.loadTexts: caciMaxPossibleEndpoints.setDescription('This object specifies the upper limit of all the possible endpoints that are allowed to be configured on this ATM switch.')
caciGenericEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4), )
if mibBuilder.loadTexts: caciGenericEndpointTable.setStatus('current')
if mibBuilder.loadTexts: caciGenericEndpointTable.setDescription('The table contains number of connection per CaciATMEndpointCategory.')
caciGenericEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciATMEndpointCategory"))
if mibBuilder.loadTexts: caciGenericEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: caciGenericEndpointEntry.setDescription('An entry in the table specifying the number of connections for the corresponding CaciATMEndpointCategory.')
caciATMEndpointCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 1), CaciATMEndpointCategory())
if mibBuilder.loadTexts: caciATMEndpointCategory.setStatus('current')
if mibBuilder.loadTexts: caciATMEndpointCategory.setDescription('Endpoint category corresponding to CaciATMEndpointCategory.')
caciTotalEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciTotalEndpoints.setStatus('current')
if mibBuilder.loadTexts: caciTotalEndpoints.setDescription('The total number of endpoints of caciATMEndpointCategory configured on this ATM switch.')
caciConnInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1), )
if mibBuilder.loadTexts: caciConnInfoTable.setStatus('current')
if mibBuilder.loadTexts: caciConnInfoTable.setDescription('The Connection Statistics table. This table has the number of connections per interface.')
caciConnInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-CONN-INFO-MIB", "caciGeneralConnEPCategory"))
if mibBuilder.loadTexts: caciConnInfoEntry.setStatus('current')
if mibBuilder.loadTexts: caciConnInfoEntry.setDescription('An entry in the caciConnInfoTable. Each entry in ifTable with ifType values: atm(37), atmLogical(80) or atmVirtual(149) has an associated entry in this table.')
caciGeneralConnEPCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 1), CaciGeneralConnEPCategory())
if mibBuilder.loadTexts: caciGeneralConnEPCategory.setStatus('current')
if mibBuilder.loadTexts: caciGeneralConnEPCategory.setDescription('The general connection or endpoint category on this ATM switch.')
caciNumUsedConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciNumUsedConns.setStatus('current')
if mibBuilder.loadTexts: caciNumUsedConns.setDescription('This object specifies the total number of used connections of type caciGeneralConnEPCategory on this interface.')
caciP2pConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1), )
if mibBuilder.loadTexts: caciP2pConnTable.setStatus('current')
if mibBuilder.loadTexts: caciP2pConnTable.setDescription('The table contains number of connection per CaciP2pConnCategory.')
caciP2pConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pConnectionCategory"))
if mibBuilder.loadTexts: caciP2pConnEntry.setStatus('current')
if mibBuilder.loadTexts: caciP2pConnEntry.setDescription('An entry in the table specifying the number of connections for the corresponding CaciP2pConnCategory.')
caciP2pConnectionCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 1), CaciP2pConnCategory())
if mibBuilder.loadTexts: caciP2pConnectionCategory.setStatus('current')
if mibBuilder.loadTexts: caciP2pConnectionCategory.setDescription('The connection category.')
caciP2pTotalConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConns.setStatus('current')
if mibBuilder.loadTexts: caciP2pTotalConns.setDescription('The total number of P2p connections of type CaciP2pConnCategory configured on this ATM switch.')
caciP2pEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1), )
if mibBuilder.loadTexts: caciP2pEndpointTable.setStatus('current')
if mibBuilder.loadTexts: caciP2pEndpointTable.setDescription('The table contains number of endpoints per CaciP2pEndpointCategory.')
caciP2pEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pEndptCategory"))
if mibBuilder.loadTexts: caciP2pEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: caciP2pEndpointEntry.setDescription('An entry in the table specifying the number of endpoints for the corresponding CaciP2pEndpointCategory.')
caciP2pEndptCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 1), CaciP2pEndpointCategory())
if mibBuilder.loadTexts: caciP2pEndptCategory.setStatus('current')
if mibBuilder.loadTexts: caciP2pEndptCategory.setDescription('The point to point endpoint category.')
caciP2pTotalConfEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConfEndpoints.setStatus('current')
if mibBuilder.loadTexts: caciP2pTotalConfEndpoints.setDescription('The number of total P2p enpoints of type CaciP2pEndpointCategory configured on this ATM switch.')
caciP2pIntEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1), )
if mibBuilder.loadTexts: caciP2pIntEndpointTable.setStatus('current')
if mibBuilder.loadTexts: caciP2pIntEndpointTable.setDescription('The table contains number of endpoints per CaciP2pIntEndpointCategory.')
caciP2pIntEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pIntEndptCategory"))
if mibBuilder.loadTexts: caciP2pIntEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: caciP2pIntEndpointEntry.setDescription('An entry in the table specifying the number of endpoints for the corresponding CaciP2pIntEndpointCategory.')
caciP2pIntEndptCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 1), CaciP2pIntEndpointCategory())
if mibBuilder.loadTexts: caciP2pIntEndptCategory.setStatus('current')
if mibBuilder.loadTexts: caciP2pIntEndptCategory.setDescription('The point to point intermediate endpoint category.')
caciP2pTotalIntEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalIntEndpoints.setStatus('current')
if mibBuilder.loadTexts: caciP2pTotalIntEndpoints.setDescription('The total number of P2p intermediate enpoints of type CaciP2pIntEndpointCategory present on this ATM switch.')
caciP2mpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1), )
if mibBuilder.loadTexts: caciP2mpConnTable.setStatus('current')
if mibBuilder.loadTexts: caciP2mpConnTable.setDescription('The table contains number of connection per CaciP2mpConnCategory.')
caciP2mpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1), ).setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2mpConnectionCategory"))
if mibBuilder.loadTexts: caciP2mpConnEntry.setStatus('current')
if mibBuilder.loadTexts: caciP2mpConnEntry.setDescription('An entry in the table specifying the number of connections for the corresponding CaciP2mpConnCategory.')
caciP2mpConnectionCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 1), CaciP2mpConnCategory())
if mibBuilder.loadTexts: caciP2mpConnectionCategory.setStatus('current')
if mibBuilder.loadTexts: caciP2mpConnectionCategory.setDescription('The point to multi point connection category.')
caciP2mpTotalConfConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2mpTotalConfConns.setStatus('current')
if mibBuilder.loadTexts: caciP2mpTotalConfConns.setDescription('The total number of P2mp connections of type CaciP2mpConnCategory configured on this ATM switch.')
ciscoAtmConnInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2))
ciscoAtmConnInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1))
ciscoAtmConnInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2))
ciscoAtmConnInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "ciscoConnInfoConfMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoTotalConnsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoTotalEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pConnsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pIntEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2mpConnsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmConnInfoMIBCompliance = ciscoAtmConnInfoMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIBCompliance.setDescription('The Compliance statement for ciscoAtm management group.')
ciscoConnInfoConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciNumUsedConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConnInfoConfMIBGroup = ciscoConnInfoConfMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoConnInfoConfMIBGroup.setDescription('Objects used for representing connection statistical details about an interface.')
ciscoP2pConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 2)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pConnsMIBGroup = ciscoP2pConnsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2pConnsMIBGroup.setDescription('Objects used for representing the point to point connections of a particular CaP2pConnCategory.')
ciscoP2pEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 3)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pEndpointsMIBGroup = ciscoP2pEndpointsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2pEndpointsMIBGroup.setDescription('Objects used for representing the point to point endpoints of a particular CaP2pEndpointCategory.')
ciscoP2pIntEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 4)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalIntEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pIntEndpointsMIBGroup = ciscoP2pIntEndpointsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2pIntEndpointsMIBGroup.setDescription('Objects used for representing the point to point intermediate endpoints of a particular CaP2pIntEndpointCategory.')
ciscoP2mpConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 5)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2mpTotalConfConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2mpConnsMIBGroup = ciscoP2mpConnsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2mpConnsMIBGroup.setDescription('Objects used for representing the point to multi point connections of a particular CaP2mpConnCategory.')
ciscoTotalConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 6)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfConns"), ("CISCO-ATM-CONN-INFO-MIB", "caciP2pMaxPossibleConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTotalConnsMIBGroup = ciscoTotalConnsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoTotalConnsMIBGroup.setDescription('Objects used for representing the total connections on the ATM switch.')
ciscoTotalEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 7)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciMaxPossibleEndpoints"), ("CISCO-ATM-CONN-INFO-MIB", "caciTotalEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTotalEndpointsMIBGroup = ciscoTotalEndpointsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoTotalEndpointsMIBGroup.setDescription('Objects used for representing the total endpoints on the ATM switch.')
mibBuilder.exportSymbols("CISCO-ATM-CONN-INFO-MIB", ciscoAtmConnInfoMIBGroups=ciscoAtmConnInfoMIBGroups, caciConnInfoTable=caciConnInfoTable, caciConnInfoEntry=caciConnInfoEntry, caciP2mpConnTable=caciP2mpConnTable, ciscoAtmConnInfoMIB=ciscoAtmConnInfoMIB, caciP2pIntEndpoints=caciP2pIntEndpoints, CaciP2mpConnCategory=CaciP2mpConnCategory, caciP2pTotalConfConns=caciP2pTotalConfConns, CaciP2pIntEndpointCategory=CaciP2pIntEndpointCategory, caciGenericEndpointTable=caciGenericEndpointTable, caciP2pConnEntry=caciP2pConnEntry, caciP2pEndpointTable=caciP2pEndpointTable, caciP2pTotalIntEndpoints=caciP2pTotalIntEndpoints, caciMIBObjects=caciMIBObjects, ciscoTotalEndpointsMIBGroup=ciscoTotalEndpointsMIBGroup, caciGenericEndpointEntry=caciGenericEndpointEntry, ciscoP2pIntEndpointsMIBGroup=ciscoP2pIntEndpointsMIBGroup, caciP2pIntEndpointEntry=caciP2pIntEndpointEntry, CaciP2pEndpointCategory=CaciP2pEndpointCategory, caciP2pMaxPossibleConns=caciP2pMaxPossibleConns, caciP2pConnTable=caciP2pConnTable, caciP2mpTotalConfConns=caciP2mpTotalConfConns, caciP2pEndpointEntry=caciP2pEndpointEntry, caciP2pConnectionCategory=caciP2pConnectionCategory, caciP2pTotalConns=caciP2pTotalConns, ciscoConnInfoConfMIBGroup=ciscoConnInfoConfMIBGroup, ciscoP2mpConnsMIBGroup=ciscoP2mpConnsMIBGroup, caciP2pTotalConfEndpoints=caciP2pTotalConfEndpoints, ciscoP2pConnsMIBGroup=ciscoP2pConnsMIBGroup, caciP2pIntEndptCategory=caciP2pIntEndptCategory, caciP2pEndpoints=caciP2pEndpoints, caciMIBNotifications=caciMIBNotifications, caciATMEndpointCategory=caciATMEndpointCategory, caciP2mpConns=caciP2mpConns, ciscoAtmConnInfoMIBConformance=ciscoAtmConnInfoMIBConformance, CaciATMEndpointCategory=CaciATMEndpointCategory, caciGeneralConnEPCategory=caciGeneralConnEPCategory, ciscoAtmConnInfoMIBCompliance=ciscoAtmConnInfoMIBCompliance, caciNumUsedConns=caciNumUsedConns, caciAtmConnInfo=caciAtmConnInfo, caciP2pEndptCategory=caciP2pEndptCategory, ciscoTotalConnsMIBGroup=ciscoTotalConnsMIBGroup, CaciP2pConnCategory=CaciP2pConnCategory, CaciGeneralConnEPCategory=CaciGeneralConnEPCategory, ciscoAtmConnInfoMIBCompliances=ciscoAtmConnInfoMIBCompliances, caciMaxPossibleEndpoints=caciMaxPossibleEndpoints, PYSNMP_MODULE_ID=ciscoAtmConnInfoMIB, caciIfInfo=caciIfInfo, caciGeneric=caciGeneric, caciP2pIntEndpointTable=caciP2pIntEndpointTable, caciP2mpConnectionCategory=caciP2mpConnectionCategory, ciscoP2pEndpointsMIBGroup=ciscoP2pEndpointsMIBGroup, caciTotalEndpoints=caciTotalEndpoints, caciP2pConns=caciP2pConns, caciP2mpConnEntry=caciP2mpConnEntry)
